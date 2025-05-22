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

# JSON dosyasını oku
with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters_data = json.load(file)

# URL'den damage_type ID
def get_damage_type_id(url):
    cur.execute("SELECT id FROM damage_types WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# URL'den ability_score ID (2024'e çevirerek)
def get_ability_score_id(url):
    if url:
        url = url.replace("/2014/", "/2024/")
        cur.execute("SELECT id FROM ability_scores WHERE url = %s", (url,))
        result = cur.fetchone()
        return result[0] if result else None
    return None

for monster in monsters_data:
    name = monster.get("name")
    cur.execute("SELECT id, legendary_actions_id FROM monsters WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue

    monster_id, legendary_actions_id = row
    if not legendary_actions_id:
        continue

    for action in monster.get("legendary_actions", []):
        action_name = action.get("name")
        description = action.get("desc")
        dc_type_id = dc_value = success_type = None
        damage_dice = damage_type_id = None

        if action.get("dc"):
            dc_type_id = get_ability_score_id(action["dc"]["dc_type"]["url"])
            dc_value = action["dc"].get("dc_value")
            success_type = action["dc"].get("success_type")

        damage = action.get("damage", [])
        if damage:
            damage_dice = damage[0].get("damage_dice")
            damage_type_id = get_damage_type_id(damage[0]["damage_type"]["url"])

        cur.execute("""
            INSERT INTO monster_legendary_actions (
                monster_id, name, description,
                dc_type_id, dc_value, success_type,
                damage_type_id, damage_dice
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            monster_id, action_name, description,
            dc_type_id, dc_value, success_type,
            damage_type_id, damage_dice
        ))

        print(f"✅ {name}: {action_name}")

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm legendary actions başarıyla yüklendi.")
