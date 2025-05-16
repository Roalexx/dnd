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

with open("jsons/5e-SRD-Monsters.json", "r") as file:
    monsters_data = json.load(file)

for monster in monsters_data:
    name = monster.get("name")

    damage_vuln = ", ".join(monster.get("damage_vulnerabilities", []))
    damage_resist = ", ".join(monster.get("damage_resistances", []))
    damage_immune = ", ".join(monster.get("damage_immunities", []))

    cur.execute("""
        UPDATE monsters SET
            damage_vulnerabilities = %s,
            damage_resistances = %s,
            damage_immunities = %s
        WHERE name = %s
    """, (damage_vuln, damage_resist, damage_immune, name))

    print(f"✅ Güncellendi: {name}")

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm canavar direnç alanları başarıyla güncellendi.")
