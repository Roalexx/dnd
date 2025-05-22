import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Damage-Types.json"

# JSON yükle
with open(json_path, "r", encoding="utf-8") as f:
    damage_types = json.load(f)

with engine.begin() as conn:
    for dmg in damage_types:
        name = dmg.get("name")
        description = "\n".join(dmg.get("desc", []))  # liste ise birleştir
        url = dmg.get("url")

        conn.execute(text("""
            INSERT INTO damage_types (name, description, url)
            VALUES (:name, :description, :url)
        """), {
            "name": name,
            "description": description,
            "url": url
        })

print("✅ Damage types başarıyla yüklendi.")
