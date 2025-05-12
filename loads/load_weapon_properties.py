import json
from sqlalchemy import create_engine, text

# PostgreSQL bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosyasının tam yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Weapon-Properties.json"

# JSON dosyasını oku
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Veriyi veritabanına yükle
with engine.begin() as conn:
    for item in data:
        name = item.get("name")
        url = item.get("url")
        desc = "\n".join(item.get("desc", []))  # listeyi metne dönüştür

        conn.execute(text("""
            INSERT INTO weapon_properties (name, description, url)
            VALUES (:name, :description, :url)
        """), {
            "name": name,
            "description": desc,
            "url": url
        })

print("✅ Weapon properties başarıyla yüklendi.")
