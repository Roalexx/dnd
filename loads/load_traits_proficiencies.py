import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Traits.json"

# JSON yükle
with open(json_path, "r", encoding="utf-8") as f:
    traits = json.load(f)

with engine.begin() as conn:
    # Tabloyu temizle
    conn.execute(text("TRUNCATE TABLE traits_proficiencies RESTART IDENTITY CASCADE"))

    for trait in traits:
        trait_url = trait.get("url")
        proficiencies = trait.get("proficiencies", [])

        if not trait_url or not proficiencies:
            continue

        # trait ID'sini bul
        trait_id_result = conn.execute(
            text("SELECT id FROM traits WHERE url = :url"),
            {"url": trait_url}
        )
        trait_id = trait_id_result.scalar()
        if not trait_id:
            continue

        for prof in proficiencies:
            prof_url = prof.get("url")
            if not prof_url:
                continue

            # proficiency ID'sini bul
            prof_id_result = conn.execute(
                text("SELECT id FROM proficiencies WHERE url = :url"),
                {"url": prof_url}
            )
            prof_id = prof_id_result.scalar()
            if not prof_id:
                continue

            # INSERT işlemi
            conn.execute(text("""
                INSERT INTO traits_proficiencies (trait_id, proficiency_id)
                VALUES (:trait_id, :proficiency_id)
            """), {
                "trait_id": trait_id,
                "proficiency_id": prof_id
            })

print("✅ traits_proficiencies tablosu başarıyla dolduruldu.")
