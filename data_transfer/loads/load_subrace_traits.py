import psycopg2
import json

# Veritabanı bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# JSON dosyasını oku
with open("jsons/5e-SRD-Subraces.json", "r") as file:
    subraces_data = json.load(file)

# Yardımcı fonksiyon: URL'den ID al
def get_id_from_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Her subrace için traits'i işle
for subrace in subraces_data:
    subrace_url = subrace.get("url")

    # subrace_id al
    cur.execute("SELECT id FROM subraces WHERE url = %s", (subrace_url,))
    row = cur.fetchone()
    if not row:
        print(f"❌ Subrace bulunamadı: {subrace_url}")
        continue

    subrace_id = row[0]

    # Trait'leri ekle
    for trait in subrace.get("racial_traits", []):
        trait_url = trait.get("url")
        trait_id = get_id_from_url("traits", trait_url)
        if trait_id:
            cur.execute("""
                INSERT INTO subrace_traits (subrace_id, trait_id)
                VALUES (%s, %s)
            """, (subrace_id, trait_id))
            print(f"✅ Eklendi: subrace_id={subrace_id}, trait_id={trait_id}")
        else:
            print(f"⚠️ Trait bulunamadı: {trait_url}")

conn.commit()
cur.close()
conn.close()
print("🚀 Tüm subrace trait verileri başarıyla yüklendi.")
