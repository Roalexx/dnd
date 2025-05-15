import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Features.json", "r", encoding="utf-8") as f:
    features_data = json.load(f)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",  # Veritabanı ismi
    user="postgres",  # Kullanıcı adı
    password="postgres",  # Parola
    host="localhost",  # Bağlantı adresi
    port="5432"  # Bağlantı portu
)
cur = conn.cursor()

# Yardımcı: URL'den ID çek (features tablosu)
def get_id_by_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Her feature için URL'yi kontrol et ve varsa ekle
for feature in features_data:
    url = feature.get("url")

    # Eğer feature.url veritabanında yoksa, ekle
    existing_feature_id = get_id_by_url("features", url)

    if not existing_feature_id:
        class_id = get_id_by_url("classes", feature["class"]["url"]) if "class" in feature else None
        description = feature.get("description", "")
        level = feature.get("level", None)
        name = feature.get("name", "")
        parent_id = feature.get("parent_id", None)
        prerequisites_id = feature.get("prerequisites_id", None)
        subclass_id = feature.get("subclass_id", None)
        feature_spesific_id = feature.get("feature_spesific_id", None)

        # Yeni veriyi `features` tablosuna ekle
        cur.execute("""
            INSERT INTO features (
                class_id, description, level, name, parent_id, prerequisites_id,
                subclass_id, url, feature_spesific_id
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            class_id, description, level, name, parent_id, prerequisites_id,
            subclass_id, url, feature_spesific_id
        ))

# Değişiklikleri kaydet
conn.commit()

# Bağlantıyı kapat
cur.close()
conn.close()
