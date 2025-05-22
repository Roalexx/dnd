import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Levels.json", "r", encoding="utf-8") as f:
    levels_data = json.load(f)

# Veritabanı bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Yardımcı fonksiyon: verilen URL'den id çek
def get_id_by_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Ana tabloya veri ekleme
for entry in levels_data:
    level = entry["level"]
    url = entry["url"]
    class_url = entry["class"]["url"]
    class_id = get_id_by_url("classes", class_url)

    subclass_id = None
    if "subclass" in entry:
        subclass_id = get_id_by_url("subclasses", entry["subclass"]["url"])

    ability_score_bonuses = entry.get("ability_score_bonuses", 0)
    prof_bonus = entry.get("prof_bonus", 0)

    cur.execute("""
        INSERT INTO levels (level, class_id, subclass_id, ability_score_bonuses, prof_bonus, url)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (level, class_id, subclass_id, ability_score_bonuses, prof_bonus, url))

# Commit ve bağlantıyı kapat
conn.commit()
cur.close()
conn.close()
