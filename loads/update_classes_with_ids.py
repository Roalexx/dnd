import psycopg2
import json

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

with open("jsons/5e-SRD-Classes.json", "r") as file:
    classes = json.load(file)

def get_ability_score_id(url):
    if url:
        url = url.replace("/2014/", "/2024/")
        cur.execute("SELECT id FROM ability_scores WHERE url = %s", (url,))
        row = cur.fetchone()
        return row[0] if row else None
    return None

update_count = 0
for cls in classes:
    name = cls.get("name")

    cur.execute("SELECT id FROM classes WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue
    id_val = row[0]

    def use_if_present(x): return id_val if x else None

    hit_die = cls.get("hit_die")
    spellcasting = cls.get("spellcasting")
    spellcasting_level = spellcasting.get("level") if spellcasting else None
    spellcasting_ability_id = get_ability_score_id(spellcasting.get("spellcasting_ability", {}).get("url")) if spellcasting else None
    spellcasting_name = spellcasting["info"][0].get("name") if spellcasting and spellcasting.get("info") else None
    spellcasting_description = "\n".join(spellcasting["info"][0].get("desc", [])) if spellcasting and spellcasting.get("info") else None

    cur.execute("""
        UPDATE classes
        SET
            hit_die = %s,
            proficiency_choices = %s,
            proficiencies = %s,
            saving_throws = %s,
            starting_equipment = %s,
            starting_equipment_options = %s,
            class_levels = %s,
            multi_classing = %s,
            spellcasting_level = %s,
            spellcasting_ability_id = %s,
            spellcasting_name = %s,
            spellcasting_description = %s
        WHERE id = %s
    """, (
        hit_die,
        use_if_present(cls.get("proficiency_choices")),
        use_if_present(cls.get("proficiencies")),
        use_if_present(cls.get("saving_throws")),
        use_if_present(cls.get("starting_equipment")),
        use_if_present(cls.get("starting_equipment_options")),
        use_if_present(cls.get("class_levels")),
        use_if_present(cls.get("multi_classing")),
        spellcasting_level,
        spellcasting_ability_id,
        spellcasting_name,
        spellcasting_description,
        id_val
    ))

    update_count += 1

conn.commit()
cur.close()
conn.close()
print(f"🎯 {update_count} sınıf başarıyla güncellendi (id üzerinden)")
