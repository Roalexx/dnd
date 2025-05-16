import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Traits.json"

with open(json_path, "r", encoding="utf-8") as f:
    traits = json.load(f)

with engine.begin() as conn:
    # DÜZELTİLDİ: tablo adı -> traits_races
    conn.execute(text("TRUNCATE TABLE traits_races RESTART IDENTITY CASCADE"))

    for trait in traits:
        trait_url = trait.get("url")
        if not trait_url:
            continue

        res = conn.execute(text("SELECT id FROM traits WHERE url = :url"), {"url": trait_url})
        trait_id = res.scalar()
        if not trait_id:
            continue

        for race in trait.get("races", []):
            race_url = race.get("url")
            if not race_url:
                continue

            res2 = conn.execute(text("SELECT id FROM races WHERE url = :url"), {"url": race_url})
            race_id = res2.scalar()
            if race_id:
                conn.execute(text("""
                    INSERT INTO traits_races (traits_id, races_id)
                    VALUES (:traits_id, :races_id)
                """), {
                    "traits_id": trait_id,
                    "races_id": race_id
                })

print("✅ traits_races tablosu başarıyla yüklendi.")
