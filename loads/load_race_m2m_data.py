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
with open("jsons/5e-SRD-Races.json", "r") as file:
    races_data = json.load(file)

# Yardımcı fonksiyon: URL'den ID al
def get_id_from_url(table, url):
    if not url:
        return None
    if table == "ability_scores":
        url = url.replace("/2014/", "/2024/")
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Tüm ırklar için many-to-many ekle
for race in races_data:
    cur.execute("SELECT id FROM races WHERE url = %s", (race["url"],))
    row = cur.fetchone()
    if not row:
        continue
    race_id = row[0]

    # 1. ability_bonus_options
    for opt in race.get("ability_bonus_options", {}).get("from", {}).get("options", []):
        ab_url = opt.get("ability_score", {}).get("url")
        ab_id = get_id_from_url("ability_scores", ab_url)
        if ab_id:
            cur.execute("""
                INSERT INTO race_ability_bonus_options (race_id, ability_score_id)
                VALUES (%s, %s)
            """, (race_id, ab_id))

    # 2. starting_proficiencies
    for prof in race.get("starting_proficiencies", []):
        prof_id = get_id_from_url("proficiencies", prof.get("url"))
        if prof_id:
            cur.execute("""
                INSERT INTO race_proficiencies (race_id, proficiency_id)
                VALUES (%s, %s)
            """, (race_id, prof_id))

    # 3. starting_proficiency_options
    for opt in race.get("starting_proficiency_options", {}).get("from", {}).get("options", []):
        item_url = opt.get("item", {}).get("url")
        prof_id = get_id_from_url("proficiencies", item_url)
        if prof_id:
            cur.execute("""
                INSERT INTO race_proficiency_options (race_id, proficiency_id)
                VALUES (%s, %s)
            """, (race_id, prof_id))

    # 4. languages
    for lang in race.get("languages", []):
        lang_id = get_id_from_url("languages", lang.get("url"))
        if lang_id:
            cur.execute("""
                INSERT INTO race_languages (race_id, language_id)
                VALUES (%s, %s)
            """, (race_id, lang_id))

    # 5. language_options
    for opt in race.get("language_options", {}).get("from", {}).get("options", []):
        item_url = opt.get("item", {}).get("url")
        lang_id = get_id_from_url("languages", item_url)
        if lang_id:
            cur.execute("""
                INSERT INTO race_language_options (race_id, language_id)
                VALUES (%s, %s)
            """, (race_id, lang_id))

    # 6. traits
    for trait in race.get("traits", []):
        trait_id = get_id_from_url("traits", trait.get("url"))
        if trait_id:
            cur.execute("""
                INSERT INTO race_traits (race_id, trait_id)
                VALUES (%s, %s)
            """, (race_id, trait_id))

    # 7. subraces
    for subrace in race.get("subraces", []):
        subrace_id = get_id_from_url("subraces", subrace.get("url"))
        if subrace_id:
            cur.execute("""
                INSERT INTO race_subraces (race_id, subrace_id)
                VALUES (%s, %s)
            """, (race_id, subrace_id))

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm many-to-many veriler başarıyla yüklendi.")
