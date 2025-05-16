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

# JSON dosyasını oku
with open("jsons/5e-SRD-Subraces.json", "r") as file:
    subraces_data = json.load(file)

# Yardımcı: URL'ye göre ID bul
def get_id_from_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Her subrace için güncelle
for subrace in subraces_data:
    url = subrace["url"]

    # URL eşleşmesi ile subrace ID'yi bul
    cur.execute("SELECT id FROM subraces WHERE url = %s", (url,))
    result = cur.fetchone()
    if not result:
        print(f"❌ URL bulunamadı: {url}")
        continue

    subrace_id = result[0]
    description = subrace.get("desc")

    # race_id
    race_url = subrace.get("race", {}).get("url")
    race_id = get_id_from_url("races", race_url) if race_url else None

    # ability_score_id (ilk ve tek kabul ediliyor)
    ability_score_id = None
    if subrace.get("ability_bonuses"):
        ability_url = subrace["ability_bonuses"][0]["ability_score"]["url"].replace("/2014/", "/2024/")
        ability_score_id = get_id_from_url("ability_scores", ability_url)

    # proficiency_id (ilk varsa)
    proficiency_id = None
    if subrace.get("starting_proficiencies"):
        prof_url = subrace["starting_proficiencies"][0]["url"]
        proficiency_id = get_id_from_url("proficiencies", prof_url)

    # trait_id (ilk varsa)
    trait_id = None
    if subrace.get("racial_traits"):
        trait_url = subrace["racial_traits"][0]["url"]
        trait_id = get_id_from_url("traits", trait_url)

    # languages: list of string (name)
    languages = []

    for lang in subrace.get("languages", []):
        name = lang.get("name")
        if name:
            languages.append(name)

    for option in subrace.get("language_options", {}).get("from", {}).get("options", []):
        item_name = option.get("item", {}).get("name")
        if item_name:
            languages.append(f"choose 1 of {item_name}")

    # UPDATE işlemi
    cur.execute("""
        UPDATE subraces
        SET description = %s,
            race_id = %s,
            ability_score_id = %s,
            proficiency_id = %s,
            trait_id = %s,
            languages = %s
        WHERE id = %s
    """, (description, race_id, ability_score_id, proficiency_id, trait_id, languages, subrace_id))

    print(f"✅ Güncellendi: {subrace['name']}")

conn.commit()
cur.close()
conn.close()
print("🚀 Tüm subrace verileri başarıyla güncellendi.")
