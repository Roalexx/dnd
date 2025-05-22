import psycopg2
import json

# DB bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# JSON verisini oku
with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters_data = json.load(file)

# damage_type.url → id
def get_damage_type_id(url):
    cur.execute("SELECT id FROM damage_types WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# JSON'daki tüm monster'lar için işle
for monster in monsters_data:
    name = monster.get("name")
    cur.execute("SELECT id, actions_id FROM monsters WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue

    monster_id, actions_id = row
    if not actions_id:
        continue

    for action in monster.get("actions", []):
        action_name = action.get("name")
        description = action.get("desc")
        damage_dice = None
        damage_type_id = None

        damage_info = action.get("damage", [])
        if damage_info:
            damage_dice = damage_info[0].get("damage_dice")
            damage_type_url = damage_info[0].get("damage_type", {}).get("url")
            damage_type_id = get_damage_type_id(damage_type_url)

        cur.execute("""
            INSERT INTO monster_actions (monster_id, name, description, damage_type, damage_dice)
            VALUES (%s, %s, %s, %s, %s)
        """, (monster_id, action_name, description, damage_type_id, damage_dice))

        print(f"✅ {name}: {action_name}")

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm monster actions başarıyla eklendi.")
