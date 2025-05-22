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

with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters_data = json.load(file)

def get_damage_type_id(url):
    cur.execute("SELECT id FROM damage_types WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

def get_ability_score_id(url):
    if url:
        url = url.replace("/2014/", "/2024/")
        cur.execute("SELECT id FROM ability_scores WHERE url = %s", (url,))
        result = cur.fetchone()
        return result[0] if result else None
    return None

for monster in monsters_data:
    name = monster.get("name")
    cur.execute("SELECT id, reactions_id FROM monsters WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue

    monster_id, reactions_id = row
    if not reactions_id:
        continue

    for reaction in monster.get("reactions", []):
        name = reaction.get("name")
        desc = reaction.get("desc")
        attack_bonus = reaction.get("attack_bonus")

        damage_dice = None
        damage_type_id = None
        dc_type_id = None
        dc_value = None
        success_type = None

        if reaction.get("damage"):
            damage_dice = reaction["damage"][0].get("damage_dice")
            damage_type_url = reaction["damage"][0].get("damage_type", {}).get("url")
            damage_type_id = get_damage_type_id(damage_type_url)

        if reaction.get("dc"):
            dc_url = reaction["dc"].get("dc_type", {}).get("url")
            dc_type_id = get_ability_score_id(dc_url)
            dc_value = reaction["dc"].get("dc_value")
            success_type = reaction["dc"].get("success_type")

        cur.execute("""
            INSERT INTO monster_reactions (
                monster_id, name, description, attack_bonus,
                damage_type_id, damage_dice,
                dc_type_id, dc_value, success_type
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            monster_id, name, desc, attack_bonus,
            damage_type_id, damage_dice,
            dc_type_id, dc_value, success_type
        ))

        print(f"✅ {monster.get('name')}: {name}")

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm monster reactions başarıyla yüklendi.")
