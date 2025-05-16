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

update_count = 0
for cls in classes:
    name = cls.get("name")
    proficiency_choices = cls.get("proficiency_choices", [])

    if not proficiency_choices:
        continue

    choice = proficiency_choices[0]  # normalde hep 1 tane var
    desc = choice.get("desc")
    choose = choice.get("choose")

    cur.execute("""
        UPDATE classes
        SET proficiency_choices_desc = %s,
            proficiency_choices_choose = %s
        WHERE name = %s
    """, (desc, choose, name))

    update_count += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {update_count} classes satırı proficiency_choices_desc ve choose ile güncellendi.")
