import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Levels.json", "r", encoding="utf-8") as f:
    levels_data = json.load(f)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Yardımcı: feature URL'den id çek
def get_feature_id_by_url(url):
    cur.execute("SELECT id FROM features WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# level_detail_features tablosunu temizleyerek başla (isteğe bağlı)
cur.execute("TRUNCATE TABLE level_detail_features RESTART IDENTITY CASCADE;")

# JSON üzerinden sırayla ilerle
for idx, entry in enumerate(levels_data, start=1):  # id sırasına göre ilerliyoruz
    features = entry.get("features", [])
    if not features:
        continue

    level_detail_id = idx  # çünkü level_detail.id sırası JSON ile birebir

    for feature in features:
        feature_url = feature.get("url")
        feature_id = get_feature_id_by_url(feature_url)
        if feature_id:
            cur.execute("""
                INSERT INTO level_detail_features (level_detail_id, feature_id)
                VALUES (%s, %s)
            """, (level_detail_id, feature_id))

# Kaydet ve kapat
conn.commit()
cur.close()
conn.close()
