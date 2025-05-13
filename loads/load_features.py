import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Features.json"

with open(json_path, "r", encoding="utf-8") as f:
    features = json.load(f)

# Birinci geçiş: insert işlemi
url_to_id = {}

with engine.begin() as conn:
    for feature in features:
        name = feature.get("name")
        level = feature.get("level")
        description = "\n".join(feature.get("desc", []))
        url = feature.get("url")

        # class_id bul
        class_url = feature.get("class", {}).get("url")
        class_id = conn.execute(
            text("SELECT id FROM classes WHERE url = :url"), {"url": class_url}
        ).scalar() if class_url else None

        # subclass_id bul
        subclass_url = feature.get("subclass", {}).get("url")
        subclass_id = conn.execute(
            text("SELECT id FROM subclasses WHERE url = :url"), {"url": subclass_url}
        ).scalar() if subclass_url else None

        # INSERT işlemi (parent_id YOK)
        result = conn.execute(text("""
            INSERT INTO features (name, level, description, url, class_id, subclass_id)
            VALUES (:name, :level, :description, :url, :class_id, :subclass_id)
            RETURNING id
        """), {
            "name": name,
            "level": level,
            "description": description,
            "url": url,
            "class_id": class_id,
            "subclass_id": subclass_id
        })

        feature_id = result.scalar()
        url_to_id[url] = feature_id  # Map URL -> ID

        # prerequisites_id ve feature_spesific_id güncelle
        conn.execute(text("""
            UPDATE features
            SET prerequisites_id = :pre_id,
                feature_spesific_id = :fs_id
            WHERE id = :id
        """), {
            "id": feature_id,
            "pre_id": feature_id if feature.get("prerequisites") else None,
            "fs_id": feature_id if feature.get("feature_specific") else None
        })

# İkinci geçiş: parent_id güncelle
with engine.begin() as conn:
    for feature in features:
        current_url = feature.get("url")
        parent_url = feature.get("parent", {}).get("url")

        if not parent_url:
            continue

        parent_id = url_to_id.get(parent_url)
        if parent_id:
            conn.execute(text("""
                UPDATE features
                SET parent_id = :parent_id
                WHERE url = :current_url
            """), {
                "parent_id": parent_id,
                "current_url": current_url
            })

print("✅ Features başarıyla yüklendi (parent güncellemeleri dahil).")
