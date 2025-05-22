import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Races.json"

with open(json_path, "r", encoding="utf-8") as f:
    races = json.load(f)

with engine.begin() as conn:
    # Tabloyu sıfırla
    conn.execute(text("TRUNCATE TABLE races RESTART IDENTITY CASCADE"))

    for race in races:
        name = race.get("name")
        url = race.get("url")

        if name and url:
            conn.execute(text("""
                INSERT INTO races (name, url)
                VALUES (:name, :url)
            """), {
                "name": name,
                "url": url
            })

print("✅ races tablosu başarıyla yüklendi.")
