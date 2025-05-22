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
        result = cur.fetchone()
        return result[0] if result else None
    return None

update_count = 0
for cls in classes:
    name = cls.get("name")
    hit_die = cls.get("hit_die")
    id_val = cls.get("id")

    def include_if(data): return id_val if data else None

    # spellcasting
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
            subclasses = %s,
            spellcasting_level = %s,
            spellcasting_ability_id = %s,
            spellcasting_name = %s,
            spellcasting_description = %s
        WHERE name = %s
    """, (
        hit_die,
        include_if(cls.get("proficiency_choices")),
        include_if(cls.get("proficiencies")),
        include_if(cls.get("saving_throws")),
        include_if(cls.get("starting_equipment")),
        include_if(cls.get("starting_equipment_options")),
        include_if(cls.get("class_levels")),
        include_if(cls.get("multi_classing")),
        include_if(cls.get("subclasses")),
        spellcasting_level,
        spellcasting_ability_id,
        spellcasting_name,
        spellcasting_description,
        name
    ))
    update_count += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 Toplam {update_count} class kaydı başarıyla güncellendi.")
