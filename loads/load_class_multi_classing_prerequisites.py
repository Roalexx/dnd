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

    # class_id'yi al
    cur.execute("SELECT id FROM classes WHERE name = %s", (name,))
    row = cur.fetchone()
    if not row:
        continue
    class_id = row[0]

    multi = cls.get("multi_classing", {})
    for prereq in multi.get("prerequisites", []):
        ability_score_url = prereq.get("ability_score", {}).get("url")
        ability_score_id = get_ability_score_id(ability_score_url)
        minimum = prereq.get("minimum_score")
        if ability_score_id and minimum is not None:
            cur.execute("""
                INSERT INTO class_multi_classing_prerequisites (class_id, ability_score_id, minimum_score)
                VALUES (%s, %s, %s)
            """, (class_id, ability_score_id, minimum))
            inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {inserted} prerequisites kaydı başarıyla eklendi.")
