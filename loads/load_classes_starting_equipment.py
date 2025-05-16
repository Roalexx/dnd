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
with open("jsons/5e-SRD-Classes.json", "r") as file:
    classes = json.load(file)

def get_equipment_id(url):
    cur.execute("SELECT id FROM equipment WHERE url = %s", (url,))
    row = cur.fetchone()
    return row[0] if row else None

inserted = 0
for cls in classes:
    name = cls.get("name")
    starting_equipment = cls.get("starting_equipment", [])

    cur.execute("SELECT id FROM classes WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue
    class_id = row[0]

    for item in starting_equipment:
        eq = item.get("equipment")
        quantity = item.get("quantity", 1)
        if not eq:
            continue

        eq_url = eq.get("url")
        equipment_id = get_equipment_id(eq_url)
        if equipment_id:
            cur.execute("""
                INSERT INTO classes_starting_equipment (class_id, equipment_id, quantity)
                VALUES (%s, %s, %s)
            """, (class_id, equipment_id, quantity))
            inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {inserted} classes_starting_equipment kaydı başarıyla eklendi.")
