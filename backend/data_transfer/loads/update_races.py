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

# Yardımcı fonksiyon: URL'den ID alma
def get_id_from_url(table, url):
    if not url:
        return None
    if table == "ability_scores":
        url = url.replace("/2014/", "/2024/")
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Güncelleme işlemi
for race in races_data:
    race_url = race["url"]
    cur.execute("SELECT id FROM races WHERE url = %s", (race_url,))
    row = cur.fetchone()
    if not row:
        print(f"❌ Race bulunamadı: {race_url}")
        continue

    race_id = row[0]
    speed = race.get("speed")

    # ability bonus
    ability_bonus = None
    ability_score_id = None
    if race.get("ability_bonuses"):
        bonus = race["ability_bonuses"][0]
        ability_bonus = bonus.get("bonus")
        ability_score_id = get_id_from_url("ability_scores", bonus["ability_score"]["url"])

    # ability bonus options
    ability_bonus_choose = None
    ability_bonus_option_id = None
    if race.get("ability_bonus_options"):
        ability_bonus_choose = race["ability_bonus_options"].get("choose")
        ability_bonus_option_id = race_id

    alignment = race.get("alignment")
    age = race.get("age")
    size = race.get("size")
    size_description = race.get("size_description")

    starting_proficiency_id = race_id if race.get("starting_proficiencies") else None
    starting_proficiency_option_id = race_id if race.get("starting_proficiency_options") else None
    language_id = race_id if race.get("languages") else None
    language_desc = race.get("language_desc")

    subrace_id = None
    if race.get("subraces"):
        subrace_id = get_id_from_url("subraces", race["subraces"][0]["url"])

    trait_id = race_id if race.get("traits") else None

    cur.execute("""
        UPDATE races SET
            speed = %s,
            ability_bonus = %s,
            ability_score_id = %s,
            ability_bonus_choose = %s,
            ability_bonus_option_id = %s,
            alignment = %s,
            age = %s,
            size = %s,
            size_description = %s,
            starting_proficiency_id = %s,
            starting_proficiency_option_id = %s,
            language_id = %s,
            language_desc = %s,
            subrace_id = %s,
            trait_id = %s
        WHERE id = %s
    """, (
        speed,
        ability_bonus,
        ability_score_id,
        ability_bonus_choose,
        ability_bonus_option_id,
        alignment,
        age,
        size,
        size_description,
        starting_proficiency_id,
        starting_proficiency_option_id,
        language_id,
        language_desc,
        subrace_id,
        trait_id,
        race_id
    ))

    print(f"✅ Güncellendi: {race['name']}")

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm races başarıyla güncellendi.")
