import json
from sqlalchemy import create_engine, text

# Veritabanı bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Rule-Sections.json"

# JSON'u yükle
with open(json_path, "r", encoding="utf-8") as f:
    sections = json.load(f)

with engine.begin() as conn:
    for section in sections:
        name = section.get("name")
        description = section.get("desc")
        url = section.get("url")

        conn.execute(text("""
            INSERT INTO rule_sections (name, description, url)
            VALUES (:name, :description, :url)
        """), {
            "name": name,
            "description": description,
            "url": url
        })

print("✅ Rule sections başarıyla yüklendi.")
