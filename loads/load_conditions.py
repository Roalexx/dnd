import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Conditions.json"

# JSON'u yükle
with open(json_path, "r", encoding="utf-8") as f:
    conditions = json.load(f)

with engine.begin() as conn:
    for cond in conditions:
        name = cond.get("name")
        desc_list = cond.get("desc", [])
        description = "\n".join(desc_list)  # listeyi tek metne çevir
        url = cond.get("url")

        conn.execute(text("""
            INSERT INTO conditions (name, description, url)
            VALUES (:name, :description, :url)
        """), {
            "name": name,
            "description": description,
            "url": url
        })

print("✅ Conditions başarıyla yüklendi.")
