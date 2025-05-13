import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosyası
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Features.json"

# JSON'u yükle
with open(json_path, "r", encoding="utf-8") as f:
    features = json.load(f)

# reference URL çıkaran fonksiyon (nested multiple/items/choice)
def extract_references_from_multiple_items(items):
    urls = []
    for item in items:
        if item.get("option_type") == "reference":
            ref_url = item.get("item", {}).get("url")
            if ref_url:
                urls.append(ref_url)
        elif item.get("option_type") == "choice":
            inner_opts = item.get("choice", {}).get("from", {}).get("options", [])
            for inner in inner_opts:
                if inner.get("option_type") == "reference":
                    ref_url = inner.get("item", {}).get("url")
                    if ref_url:
                        urls.append(ref_url)
    return urls

with engine.begin() as conn:
    for feature in features:
        fs = feature.get("feature_specific")
        url = feature.get("url")

        if not fs or "expertise_options" not in fs or not url:
            continue

        # feature id
        result = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": url})
        feature_id = result.scalar()
        if feature_id is None:
            continue

        # feature_specific.expertise_id alınır
        result2 = conn.execute(text("""
            SELECT expertise_id FROM feature_specific
            WHERE feature_specific_id = :fid
        """), {"fid": feature_id})
        expertise_id = result2.scalar()
        if expertise_id is None:
            continue

        # sadece 2. seçenekten al
        options = fs.get("expertise_options", {}).get("from", {}).get("options", [])
        if len(options) < 2 or options[1].get("option_type") != "multiple":
            continue

        items = options[1].get("items", [])
        ref_urls = extract_references_from_multiple_items(items)

        for ref_url in ref_urls:
            result3 = conn.execute(text("SELECT id FROM proficiencies WHERE url = :url"), {"url": ref_url})
            proficiency_id = result3.scalar()
            if proficiency_id is None:
                continue

            # tekrar varsa insert etme
            exists = conn.execute(text("""
                SELECT 1 FROM expertises
                WHERE expertise_id = :expertise_id AND proficiency_id = :proficiency_id
            """), {
                "expertise_id": expertise_id,
                "proficiency_id": proficiency_id
            }).scalar()

            if exists:
                continue

            # INSERT
            conn.execute(text("""
                INSERT INTO expertises (expertise_id, proficiency_id)
                VALUES (:expertise_id, :proficiency_id)
            """), {
                "expertise_id": expertise_id,
                "proficiency_id": proficiency_id
            })

print("✅ expertises güncellendi: sadece 2. option’dan yeni kayıtlar eklendi, eskiler korundu.")
