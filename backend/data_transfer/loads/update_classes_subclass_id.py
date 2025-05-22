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

# JSON yükle
with open("jsons/5e-SRD-Classes.json", "r") as file:
    classes = json.load(file)

update_count = 0
for cls in classes:
    name = cls.get("name")
    subclasses = cls.get("subclasses", [])
    if not subclasses:
        continue

    subclass_url = subclasses[0].get("url")
    if not subclass_url:
        continue

    # URL ile subclass_id bul
    cur.execute("SELECT id FROM subclasses WHERE url = %s", (subclass_url,))
    row = cur.fetchone()
    if not row:
        continue

    subclass_id = row[0]

    # Güncelle
    cur.execute("""
        UPDATE classes
        SET subclass_id = %s
        WHERE name = %s
    """, (subclass_id, name))

    update_count += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 Toplam {update_count} class satırına subclass_id başarıyla eklendi.")
