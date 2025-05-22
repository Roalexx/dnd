import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON verisi
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Features.json"
with open(json_path, "r", encoding="utf-8") as f:
    features_json = json.load(f)

# JSON verilerini URL ile eşle
json_map = {feature["url"]: feature for feature in features_json}

with engine.begin() as conn:
    # 371 ve üstü id'leri al
    result = conn.execute(text("SELECT id, url FROM features WHERE id >= 371"))
    features_to_update = result.fetchall()

    for row in features_to_update:
        feature_id, url = row

        feature = json_map.get(url)
        if not feature:
            print(f"❌ JSON'da {url} bulunamadı, atlanıyor.")
            continue

        name = feature.get("name")
        level = feature.get("level")
        description = "\n".join(feature.get("desc", []))
        class_url = feature.get("class", {}).get("url")
        subclass_url = feature.get("subclass", {}).get("url")

        # class_id bul
        class_id = conn.execute(
            text("SELECT id FROM classes WHERE url = :url"), {"url": class_url}
        ).scalar() if class_url else None

        # subclass_id bul
        subclass_id = conn.execute(
            text("SELECT id FROM subclasses WHERE url = :url"), {"url": subclass_url}
        ).scalar() if subclass_url else None

        # prerequisites ve feature_specific tablolarında ilgili id var mı kontrol et
        pre_id = (
            feature_id if feature.get("prerequisites") and
            conn.execute(text("SELECT 1 FROM prerequisites WHERE id = :id"), {"id": feature_id}).first()
            else None
        )

        fs_id = (
            feature_id if feature.get("feature_specific") and
            conn.execute(text("SELECT 1 FROM feature_specific WHERE id = :id"), {"id": feature_id}).first()
            else None
        )

        # Güncelle
        conn.execute(text("""
            UPDATE features
            SET name = :name,
                level = :level,
                description = :description,
                class_id = :class_id,
                subclass_id = :subclass_id,
                prerequisites_id = :pre_id,
                feature_spesific_id = :fs_id
            WHERE id = :id
        """), {
            "id": feature_id,
            "name": name,
            "level": level,
            "description": description,
            "class_id": class_id,
            "subclass_id": subclass_id,
            "pre_id": pre_id,
            "fs_id": fs_id
        })

    # Parent ID güncellemesi
    for row in features_to_update:
        feature_id, url = row
        feature = json_map.get(url)
        if not feature:
            continue

        parent_url = feature.get("parent", {}).get("url")
        if not parent_url:
            continue

        parent_id = conn.execute(
            text("SELECT id FROM features WHERE url = :url"), {"url": parent_url}
        ).scalar()

        if parent_id:
            conn.execute(text("""
                UPDATE features
                SET parent_id = :parent_id
                WHERE id = :id
            """), {
                "parent_id": parent_id,
                "id": feature_id
            })

print("✅ Features tablosunda id >= 371 olan tüm kayıtlar başarıyla güncellendi.")
