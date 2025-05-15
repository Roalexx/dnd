import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Spells.json", "r", encoding="utf-8") as f:
    spells_data = json.load(f)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Yardımcı: URL'den ID çek (classes tablosu)
def get_id_by_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# spells_classes tablosuna class verilerini ekle
for i, spell in enumerate(spells_data):
    spell_id = i + 1

    # `classes` listesine her class'ı ekle
    if "classes" in spell:
        for class_data in spell["classes"]:
            class_id = get_id_by_url("classes", class_data["url"])

            if class_id:
                cur.execute("""
                    INSERT INTO spells_classes (spells_id, classes_id)
                    VALUES (%s, %s)
                """, (spell_id, class_id))

# Değişiklikleri kaydet
conn.commit()
cur.close()
conn.close()
