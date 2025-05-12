import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Ability-Scores.json"

# JSON yükle
with open(json_path, "r", encoding="utf-8") as f:
    abilities = json.load(f)

with engine.begin() as conn:
    for ab in abilities:
        name = ab.get("name")
        full_name = ab.get("full_name")
        description = "\n".join(ab.get("description", []))
        url = ab.get("url")

        conn.execute(text("""
            INSERT INTO ability_scores (name, full_name, description, url)
            VALUES (:name, :full_name, :description, :url)
        """), {
            "name": name,
            "full_name": full_name,
            "description": description,
            "url": url
        })

print("✅ Ability scores başarıyla yüklendi.")
