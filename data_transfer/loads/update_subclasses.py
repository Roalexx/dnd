import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Subclasses.json", "r", encoding="utf-8") as f:
    subclasses_data = json.load(f)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Yardımcı: URL'den ID çek (classes ve subclasses tablosu)
def get_id_by_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# subclasses tablosuna verileri güncelleyelim
for subclass in subclasses_data:
    subclass_id = get_id_by_url("subclasses", subclass["url"])

    # class_id'yi alıyoruz
    class_id = get_id_by_url("classes", subclass["class"]["url"])

    # sadece class_id, spells_id, description ve subclass_flavor'ı güncelleyeceğiz
    description = subclass["desc"] if "desc" in subclass else None
    subclass_flavor = subclass["subclass_flavor"] if "subclass_flavor" in subclass else None

    if class_id and subclass_id:
        cur.execute("""
            UPDATE subclasses
            SET class_id = %s, spells_id = %s, description = %s, subclass_flavor = %s
            WHERE id = %s
        """, (class_id, subclass_id, description, subclass_flavor, subclass_id))

# Değişiklikleri kaydet
conn.commit()
cur.close()
conn.close()
