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

# Yardımcı fonksiyon: url'den ID al
def get_id_from_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Her subrace için proficiency'leri işle
for subrace in subraces_data:
    subrace_url = subrace.get("url")

    # subraces tablosundan id bul
    cur.execute("SELECT id FROM subraces WHERE url = %s", (subrace_url,))
    result = cur.fetchone()
    if not result:
        print(f"❌ Subrace bulunamadı: {subrace_url}")
        continue
    subrace_id = result[0]

    # Her proficiency için FK id bul ve insert et
    for prof in subrace.get("starting_proficiencies", []):
        prof_url = prof.get("url")
        prof_id = get_id_from_url("proficiencies", prof_url)
        if prof_id:
            cur.execute("""
                INSERT INTO subrace_proficiencies (subrace_id, proficiency_id)
                VALUES (%s, %s)
            """, (subrace_id, prof_id))
            print(f"✅ Eklendi: subrace_id={subrace_id}, proficiency_id={prof_id}")
        else:
            print(f"⚠️ Proficiency bulunamadı, NULL geçildi: {prof_url}")

conn.commit()
cur.close()
conn.close()
print("🚀 Tüm starting_proficiencies başarıyla yüklendi.")
