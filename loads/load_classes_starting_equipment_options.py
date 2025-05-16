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

def get_equipment_id(url):
    cur.execute("SELECT id FROM equipment WHERE url = %s", (url,))
    row = cur.fetchone()
    return row[0] if row else None

inserted = 0
for cls in classes:
    name = cls.get("name")
    cur.execute("SELECT id FROM classes WHERE name = %s", (name,))
    result = cur.fetchone()
    if not result:
        continue
    class_id = result[0]

    equipment_options = cls.get("starting_equipment_options", [])
    for group in equipment_options:
        options = group.get("from", {}).get("options", [])
        for opt in options:
            # Tipine göre ayrıştır
            if opt["option_type"] == "counted_reference":
                url = opt["of"]["url"]
            elif opt["option_type"] == "reference":
                url = opt["item"]["url"]
            elif opt["option_type"] == "multiple":
                for subitem in opt.get("items", []):
                    if subitem["option_type"] == "counted_reference":
                        url = subitem["of"]["url"]
                        eq_id = get_equipment_id(url)
                        if eq_id:
                            cur.execute("""
                                INSERT INTO classes_starting_equipment_options (class_id, equipment_id)
                                VALUES (%s, %s)
                            """, (class_id, eq_id))
                            inserted += 1
                continue
            else:
                continue

            eq_id = get_equipment_id(url)
            if eq_id:
                cur.execute("""
                    INSERT INTO classes_starting_equipment_options (class_id, equipment_id)
                    VALUES (%s, %s)
                """, (class_id, eq_id))
                inserted += 1

conn.commit()
cur.close()
conn.close()
print(f"🎯 {inserted} classes_starting_equipment_options kaydı başarıyla eklendi.")
