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

# Temizle ve ID sıfırla
cur.execute("TRUNCATE TABLE monster_spells RESTART IDENTITY CASCADE;")
conn.commit()

# JSON oku
with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters = json.load(file)

# URL'den spell_id al
def get_spell_id(url):
    cur.execute("SELECT id FROM spells WHERE url = %s", (url,))
    row = cur.fetchone()
    return row[0] if row else None

# monster name → id map oluştur
cur.execute("SELECT id, name FROM monsters")
monster_map = {row[1]: row[0] for row in cur.fetchall()}

# monsters_special_abilities üzerinden spellcasting girdilerini bul
cur.execute("""
    SELECT id, monster_id FROM monsters_special_abilities
    WHERE name = 'Spellcasting'
""")
rows = cur.fetchall()

insert_count = 0

for special_ability_id, monster_id in rows:
    # Canavarın adını bul
    monster_name = next((name for name, mid in monster_map.items() if mid == monster_id), None)
    if not monster_name:
        continue

    # JSON'dan canavar verisini bul
    monster_data = next((m for m in monsters if m.get("name") == monster_name), None)
    if not monster_data:
        continue

    for ability in monster_data.get("special_abilities", []):
        if ability.get("name", "").lower() == "spellcasting" and "spellcasting" in ability:
            for spell in ability["spellcasting"].get("spells", []):
                spell_url = spell.get("url")
                spell_id = get_spell_id(spell_url)
                if spell_id:
                    cur.execute("""
                        INSERT INTO monster_spells (monster_special_ability_id, spell_id)
                        VALUES (%s, %s)
                    """, (special_ability_id, spell_id))
                    insert_count += 1

conn.commit()
cur.close()
conn.close()
print(f"🎯 {insert_count} monster_spell kaydı başarıyla yüklendi.")
