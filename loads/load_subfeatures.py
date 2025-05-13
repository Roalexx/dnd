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
    # subfeatures tablosunu sıfırla
    conn.execute(text("TRUNCATE TABLE subfeatures RESTART IDENTITY CASCADE"))

    for feature in features:
        fs = feature.get("feature_specific")
        url = feature.get("url")

        if not fs or "subfeature_options" not in fs or not url:
            continue

        sub_opt = fs["subfeature_options"]
        if "from" not in sub_opt or "options" not in sub_opt["from"]:
            continue

        # features.url → features.id (ana feature)
        result = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": url})
        feature_id_fk = result.scalar()
        if feature_id_fk is None:
            continue

        # feature_specific.subfeature_id alınır
        result2 = conn.execute(text("""
            SELECT subfeature_id FROM feature_specific
            WHERE feature_specific_id = :fid
        """), {"fid": feature_id_fk})
        subfeature_id = result2.scalar()
        if subfeature_id is None:
            continue

        # alt feature'ların id'lerini al
        for opt in sub_opt["from"]["options"]:
            item = opt.get("item", {})
            item_url = item.get("url")
            if not item_url:
                continue

            result3 = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": item_url})
            target_feature_id = result3.scalar()
            if target_feature_id is None:
                continue

            # INSERT
            conn.execute(text("""
                INSERT INTO subfeatures (subfeature_id, feature_id)
                VALUES (:subfeature_id, :feature_id)
            """), {
                "subfeature_id": subfeature_id,
                "feature_id": target_feature_id
            })

print("✅ subfeatures tablosu (subfeature_id = feature_specific.subfeature_id) olarak başarıyla dolduruldu.")
