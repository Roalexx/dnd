import psycopg2
import json

# Veritabanı bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Temizle + ID sıfırla
cur.execute("TRUNCATE TABLE monsters_special_abilities RESTART IDENTITY CASCADE;")
conn.commit()

# JSON oku
with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters = json.load(file)

# Yardımcı FK eşleştiriciler
def get_damage_type_id(url):
    cur.execute("SELECT id FROM damage_types WHERE url = %s", (url,))
    row = cur.fetchone()
    return row[0] if row else None

def get_ability_score_id(url):
    if url:
        url = url.replace("/2014/", "/2024/")
        cur.execute("SELECT id FROM ability_scores WHERE url = %s", (url,))
        row = cur.fetchone()
        return row[0] if row else None
    return None

insert_count = 0
for monster in monsters:
    name = monster.get("name")
    cur.execute("SELECT id, special_abilities_id FROM monsters WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue

    monster_id, special_abilities_id = row
    if not special_abilities_id:
        continue

    for ability in monster.get("special_abilities", []):
        ability_name = ability.get("name")
        description = ability.get("desc")

        damage_dice = None
        damage_type_id = None
        dc_type_id = None
        dc_value = None
        success_type = None

        spellcasting_level = None
        spellcasting_ability_score_id = None
        spellcasting_modifier = None
        spellcasting_components_required = None
        spellcasting_school = None
        spellcasting_slots = None
        spellcasting_spells = None  # bu kolon ileride m2m ilişki için kullanılacak

        # damage
        if ability.get("damage"):
            dmg = ability["damage"][0]
            damage_dice = dmg.get("damage_dice")
            damage_type_id = get_damage_type_id(dmg.get("damage_type", {}).get("url"))

        # dc
        if ability.get("dc"):
            dc = ability["dc"]
            dc_type_id = get_ability_score_id(dc.get("dc_type", {}).get("url"))
            dc_value = dc.get("dc_value")
            success_type = dc.get("success_type")

        # spellcasting içeriği
        spellcasting = ability.get("spellcasting")
        if spellcasting:
            spellcasting_level = spellcasting.get("level")
            spellcasting_modifier = spellcasting.get("modifier")
            spellcasting_components_required = ", ".join(spellcasting.get("components_required", [])) if spellcasting.get("components_required") else None
            spellcasting_school = spellcasting.get("school")
            if spellcasting.get("slots"):
                spellcasting_slots = ", ".join(f"{k}: {v}" for k, v in spellcasting["slots"].items())
            spellcasting_ability_score_id = get_ability_score_id(spellcasting.get("ability", {}).get("url"))
            spellcasting_spells = None  # sonra doldurulacak

        cur.execute("""
            INSERT INTO monsters_special_abilities (
                monster_id, name, description,
                damage_type_id, damage_dice,
                dc_type_id, dc_value, success_type,
                spellcasting_level, spellcasting_ability_score_id,
                spellcasting_modifier, spellcasting_components_required,
                spellcasting_school, spellcasting_slots, spellcasting_spells
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            monster_id, ability_name, description,
            damage_type_id, damage_dice,
            dc_type_id, dc_value, success_type,
            spellcasting_level, spellcasting_ability_score_id,
            spellcasting_modifier, spellcasting_components_required,
            spellcasting_school, spellcasting_slots, None
        ))

        insert_count += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {insert_count} özel yetenek (spellcasting dahil) başarıyla yüklendi.")
