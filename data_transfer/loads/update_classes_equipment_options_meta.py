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

update_count = 0
for cls in classes:
    name = cls.get("name")
    equipment_options = cls.get("starting_equipment_options", [])

    if not equipment_options:
        continue

    option = equipment_options[0]
    choose = option.get("choose")
    desc = option.get("desc")

    cur.execute("""
        UPDATE classes
        SET starting_equipment_options_choose = %s,
            starting_equipment_options_desc = %s
        WHERE name = %s
    """, (choose, desc, name))

    update_count += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {update_count} classes satırı options_desc ve choose ile güncellendi.")
