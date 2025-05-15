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

# Yardımcı: URL'den ID çek (ability_scores tablosu)
def get_id_by_url(table, url):
    # /api/2024 üzerinden URL eşlemesi yapıyoruz
    url_2024 = url.replace("/api/2014/", "/api/2024/")
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url_2024,))
    result = cur.fetchone()
    return result[0] if result else None

# dc_id'yi güncellemek için
for i, spell in enumerate(spells_data):
    spell_id = i + 1

    # dc_id için doğru URL eşlemesi (2024 üzerinden eşleştiriyoruz)
    if "dc" in spell and "dc_type" in spell["dc"]:
        dc_url = spell["dc"]["dc_type"]["url"]
        dc_id = get_id_by_url("ability_scores", dc_url)  # 2024 üzerindeki ability_scores.url ile dc_id'yi alıyoruz
    else:
        dc_id = None

    # dc_id'yi güncelleme işlemi
    if dc_id is not None:
        cur.execute("""
            UPDATE spells
            SET dc_id = %s
            WHERE id = %s
        """, (dc_id, spell_id))

# Değişiklikleri kaydet
conn.commit()
cur.close()
conn.close()
