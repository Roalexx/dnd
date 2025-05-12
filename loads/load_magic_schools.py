import json
from sqlalchemy import create_engine, text

# Veritabanı bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Magic-Schools.json"

# JSON verisini yükle
with open(json_path, "r", encoding="utf-8") as f:
    schools = json.load(f)

with engine.begin() as conn:
    for school in schools:
        name = school.get("name")
        description = school.get("desc")
        url = school.get("url")

        conn.execute(text("""
            INSERT INTO magic_schools (name, description, url)
            VALUES (:name, :description, :url)
        """), {
            "name": name,
            "description": description,
            "url": url
        })

print("✅ Magic schools başarıyla yüklendi.")
