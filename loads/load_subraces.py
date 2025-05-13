import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Subraces.json"

with open(json_path, "r", encoding="utf-8") as f:
    subraces = json.load(f)

with engine.begin() as conn:
    # Tabloyu temizle
    conn.execute(text("TRUNCATE TABLE subraces RESTART IDENTITY CASCADE"))

    for subrace in subraces:
        name = subrace.get("name")
        url = subrace.get("url")

        if name and url:
            conn.execute(text("""
                INSERT INTO subraces (name, url)
                VALUES (:name, :url)
            """), {
                "name": name,
                "url": url
            })

print("✅ subraces tablosu başarıyla yüklendi.")
