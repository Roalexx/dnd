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

# Yardımcı: URL'den ID çek (subclasses tablosu)
def get_id_by_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# spells_subclasses tablosuna subclass verilerini ekle
for i, spell in enumerate(spells_data):
    spell_id = i + 1

    # `subclasses` listesine her subclass'ı ekle
    if "subclasses" in spell:
        for subclass_data in spell["subclasses"]:
            subclass_id = get_id_by_url("subclasses", subclass_data["url"])

            if subclass_id:
                cur.execute("""
                    INSERT INTO spells_subclasses (spells_id, subclasses_id)
                    VALUES (%s, %s)
                """, (spell_id, subclass_id))

# Değişiklikleri kaydet
conn.commit()
cur.close()
conn.close()
