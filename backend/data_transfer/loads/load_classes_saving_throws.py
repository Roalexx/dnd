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

# ability_scores.url → id dönüşümü (2024)
def get_ability_score_id(url):
    if url:
        url = url.replace("/2014/", "/2024/")
        cur.execute("SELECT id FROM ability_scores WHERE url = %s", (url,))
        row = cur.fetchone()
        return row[0] if row else None
    return None

inserted = 0
for cls in classes:
    name = cls.get("name")
    saving_throws = cls.get("saving_throws", [])

    cur.execute("SELECT id FROM classes WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue
    class_id = row[0]

    for throw in saving_throws:
        ability_url = throw.get("url")
        ability_score_id = get_ability_score_id(ability_url)
        if ability_score_id:
            cur.execute("""
                INSERT INTO classes_saving_throws (class_id, ability_score_id)
                VALUES (%s, %s)
            """, (class_id, ability_score_id))
            inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {inserted} saving throw kaydı classes_saving_throws tablosuna başarıyla eklendi.")
