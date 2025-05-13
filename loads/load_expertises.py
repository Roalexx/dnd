import json
from sqlalchemy import create_engine, text

# PostgreSQL bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Features.json"

# JSON'u yükle
with open(json_path, "r", encoding="utf-8") as f:
    features = json.load(f)

with engine.begin() as conn:
    # expertises tablosunu sıfırla
    conn.execute(text("TRUNCATE TABLE expertises RESTART IDENTITY CASCADE"))

    for feature in features:
        fs = feature.get("feature_specific")
        url = feature.get("url")

        if not fs or "expertise_options" not in fs or not url:
            continue

        # features.url → features.id
        result = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": url})
        feature_id_fk = result.scalar()
        if feature_id_fk is None:
            continue

        # features.id → feature_specific.feature_specific_id → expertise_id
        result2 = conn.execute(text("""
            SELECT expertise_id FROM feature_specific
            WHERE feature_specific_id = :fid
        """), {"fid": feature_id_fk})
        expertise_id = result2.scalar()
        if expertise_id is None:
            continue

        # JSON'daki proficiency URL'lerini al
        options = fs["expertise_options"].get("from", {}).get("options", [])
        for opt in options:
            item = opt.get("item", {})
            item_url = item.get("url")
            if not item_url:
                continue

            # proficiency_id bul
            result3 = conn.execute(text("SELECT id FROM proficiencies WHERE url = :url"), {"url": item_url})
            proficiency_id = result3.scalar()
            if proficiency_id is None:
                continue

            # INSERT
            conn.execute(text("""
                INSERT INTO expertises (expertise_id, proficiency_id)
                VALUES (:expertise_id, :proficiency_id)
            """), {
                "expertise_id": expertise_id,
                "proficiency_id": proficiency_id
            })

print("✅ expertises tablosu başarıyla oluşturuldu.")
