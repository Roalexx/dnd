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

# JSON yükle
with open("jsons/5e-SRD-Classes.json", "r") as file:
    classes = json.load(file)

def get_proficiency_id(url):
    cur.execute("SELECT id FROM proficiencies WHERE url = %s", (url,))
    row = cur.fetchone()
    return row[0] if row else None

inserted = 0
for cls in classes:
    name = cls.get("name")
    profs = cls.get("proficiencies", [])

    cur.execute("SELECT id FROM classes WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue
    class_id = row[0]

    for prof in profs:
        prof_url = prof.get("url")
        proficiency_id = get_proficiency_id(prof_url)
        if proficiency_id:
            cur.execute("""
                INSERT INTO classes_proficiencies (class_id, proficiency_id)
                VALUES (%s, %s)
            """, (class_id, proficiency_id))
            inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {inserted} classes_proficiencies kaydı başarıyla eklendi.")
