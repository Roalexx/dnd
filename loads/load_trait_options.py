import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Traits.json"

with open(json_path, "r", encoding="utf-8") as f:
    traits = json.load(f)

with engine.begin() as conn:
    # Tabloyu temizle
    conn.execute(text("TRUNCATE TABLE trait_options RESTART IDENTITY CASCADE"))

    for trait in traits:
        trait_url = trait.get("url")
        if not trait_url:
            continue

        # trait_proficiency_id'yi bul (option_id olarak kullanılacak)
        res = conn.execute(text("SELECT trait_proficiency_id FROM traits WHERE url = :url"), {"url": trait_url})
        option_id = res.scalar()
        if not option_id:
            continue

        # 1. proficiency_choices
        prof_choices = trait.get("proficiency_choices")
        if prof_choices:
            choose = prof_choices.get("choose")
            choice_type = prof_choices.get("type")
            options = prof_choices.get("from", {}).get("options", [])
            for opt in options:
                url = opt.get("item", {}).get("url")
                if not url:
                    continue
                res = conn.execute(text("SELECT id FROM proficiencies WHERE url = :url"), {"url": url})
                prof_id = res.scalar()
                if prof_id:
                    conn.execute(text("""
                        INSERT INTO trait_options (choose, type, option_id, proficiency_id)
                        VALUES (:choose, :type, :option_id, :proficiency_id)
                    """), {
                        "choose": choose,
                        "type": choice_type,
                        "option_id": option_id,
                        "proficiency_id": prof_id
                    })

        # 2. trait_specific.spell_options / subtrait_options
        ts = trait.get("trait_specific")
        if isinstance(ts, dict):
            for key, data in ts.items():
                if not key.endswith("_options"):
                    continue
                choose = data.get("choose")
                choice_type = data.get("type")
                options = data.get("from", {}).get("options", [])
                for opt in options:
                    item = opt.get("item", {})
                    url = item.get("url")
                    if not url:
                        continue

                    # URL'ye göre ilgili tablonun ID'si
                    if choice_type == "spell":
                        res = conn.execute(text("SELECT id FROM spells WHERE url = :url"), {"url": url})
                        spell_id = res.scalar()
                        if spell_id:
                            conn.execute(text("""
                                INSERT INTO trait_options (choose, type, option_id, spell_id)
                                VALUES (:choose, :type, :option_id, :spell_id)
                            """), {
                                "choose": choose,
                                "type": choice_type,
                                "option_id": option_id,
                                "spell_id": spell_id
                            })

                    elif choice_type == "trait":
                        res = conn.execute(text("SELECT id FROM traits WHERE url = :url"), {"url": url})
                        subtrait_id = res.scalar()
                        if subtrait_id:
                            conn.execute(text("""
                                INSERT INTO trait_options (choose, type, option_id, subtrait_id)
                                VALUES (:choose, :type, :option_id, :subtrait_id)
                            """), {
                                "choose": choose,
                                "type": choice_type,
                                "option_id": option_id,
                                "subtrait_id": subtrait_id
                            })

print("✅ trait_options tablosu başarıyla dolduruldu.")
