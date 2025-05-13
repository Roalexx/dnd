import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Spells.json"

with open(json_path, "r", encoding="utf-8") as f:
    spells = json.load(f)

with engine.begin() as conn:
    # Tabloyu sıfırla
    conn.execute(text("TRUNCATE TABLE spells RESTART IDENTITY CASCADE"))

    for spell in spells:
        name = spell.get("name")
        url = spell.get("url")

        if name and url:
            conn.execute(text("""
                INSERT INTO spells (name, url)
                VALUES (:name, :url)
            """), {
                "name": name,
                "url": url
            })

print("✅ spells tablosu başarıyla yüklendi.")
