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

# JSON verisini oku
with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters_data = json.load(file)

# condition.url → id
def get_condition_id(url):
    cur.execute("SELECT id FROM conditions WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

for monster in monsters_data:
    name = monster.get("name")

    # monster_id ve prof_id kontrolü
    cur.execute("SELECT id, condition_immunities_id FROM monsters WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue

    monster_id, condition_immunities_id = row
    if not condition_immunities_id:
        continue

    for condition in monster.get("condition_immunities", []):
        condition_url = condition.get("url")
        condition_id = get_condition_id(condition_url)
        if not condition_id:
            print(f"⚠️ Condition bulunamadı: {condition_url}")
            continue

        cur.execute("""
            INSERT INTO monster_condition_immunities (monster_id, condition_id)
            VALUES (%s, %s)
        """, (monster_id, condition_id))

        print(f"✅ {name}: {condition.get('name')}")

conn.commit()
cur.close()
conn.close()
print("🎯 Condition immunities başarıyla yüklendi.")
