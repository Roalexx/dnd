import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Subclasses.json", "r", encoding="utf-8") as f:
    subclasses_data = json.load(f)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Yardımcı: URL'den ID çek (spells, levels, features tablosu)
def get_id_by_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# spells_subclasses tablosuna verileri güncelleyelim
for subclass in subclasses_data:
    subclass_id = get_id_by_url("subclasses", subclass["url"])

    if subclass_id:
        # Subclass'ı spells_subclasses tablosuna ekleyelim
        for spell_data in subclass.get("spells", []):
            spell_url = spell_data["spell"]["url"]
            spell_id = get_id_by_url("spells", spell_url)

            # prerequisites listesine dönüştürüp birleştiriyoruz
            required_level_id = None
            required_feature_id = None
            if "prerequisites" in spell_data:
                for prereq in spell_data["prerequisites"]:
                    if prereq["type"] == "level":
                        required_level_id = get_id_by_url("levels", prereq["url"])
                    elif prereq["type"] == "feature":
                        required_feature_id = get_id_by_url("features", prereq["url"])

            if spell_id:
                cur.execute("""
                    UPDATE spells_subclasses
                    SET required_level_id = %s, required_feature_id = %s
                    WHERE spells_id = %s AND subclasses_id = %s
                """, (required_level_id, required_feature_id, spell_id, subclass_id))

# Değişiklikleri kaydet
conn.commit()
cur.close()
conn.close()
