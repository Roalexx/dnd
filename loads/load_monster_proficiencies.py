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

# JSON dosyasını oku
with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters_data = json.load(file)

# proficiency.url'den ID al
def get_proficiency_id(url):
    cur.execute("SELECT id FROM proficiencies WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

for monster in monsters_data:
    name = monster.get("name")
    cur.execute("SELECT id, proficiencies_id FROM monsters WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue

    monster_id, proficiencies_id = row
    if not proficiencies_id:
        continue

    for entry in monster.get("proficiencies", []):
        prof_url = entry["proficiency"]["url"]
        value = entry.get("value")

        proficiency_id = get_proficiency_id(prof_url)
        if not proficiency_id:
            print(f"❌ Proficiency bulunamadı: {prof_url}")
            continue

        cur.execute("""
            INSERT INTO monster_proficiencies (monster_id, proficiency_id, proficiency_value)
            VALUES (%s, %s, %s)
        """, (monster_id, proficiency_id, value))

        print(f"✅ {name}: {entry['proficiency']['name']} +{value}")

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm monster proficiency verileri başarıyla yüklendi.")
