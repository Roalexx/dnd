import psycopg2
import json

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

def dict_to_str(d):
    return ', '.join(f"{k}: {v}" for k, v in d.items()) if isinstance(d, dict) else None

for monster in monsters_data:
    name = monster.get("name")
    size = monster.get("size")
    type_ = monster.get("type")
    subtype = monster.get("subtype")
    alignment = monster.get("alignment")
    hit_points = monster.get("hit_points")
    hit_dice = monster.get("hit_dice")
    xp = monster.get("xp")
    challenge_rating = monster.get("challenge_rating")
    strength = monster.get("strength")
    dexterity = monster.get("dexterity")
    constitution = monster.get("constitution")
    intelligence = monster.get("intelligence")
    wisdom = monster.get("wisdom")
    charisma = monster.get("charisma")
    languages = monster.get("languages")
    proficiency_bonus = monster.get("proficiency_bonus")
    senses = dict_to_str(monster.get("senses", {}))
    speed = dict_to_str(monster.get("speed", {}))

    ac = monster.get("armor_class", [])
    if isinstance(ac, list) and ac:
        armor_class_type = ac[0].get("type")
        armor_class_value = ac[0].get("value")
    elif isinstance(ac, int):
        armor_class_type = None
        armor_class_value = ac
    else:
        armor_class_type = None
        armor_class_value = None

    # İlk olarak monster'ı ekle ve ID'yi al
    cur.execute("""
        INSERT INTO monsters (
            name, size, type, subtype, alignment,
            armor_class_type, armor_class_value,
            hit_points, hit_dice, xp, challenge_rating,
            strength, dexterity, constitution, intelligence, wisdom, charisma,
            languages, proficiency_bonus, senses, speed
        ) VALUES (
            %s, %s, %s, %s, %s,
            %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s
        )
        RETURNING id
    """, (
        name, size, type_, subtype, alignment,
        armor_class_type, armor_class_value,
        hit_points, hit_dice, xp, challenge_rating,
        strength, dexterity, constitution, intelligence, wisdom, charisma,
        languages, proficiency_bonus, senses, speed
    ))

    monster_id = cur.fetchone()[0]

    # M2M kolonları: varsa monster_id, yoksa NULL
    m2m_data = {
        "proficiencies_id": monster_id if monster.get("proficiencies") else None,
        "damage_vulnerabilities_id": monster_id if monster.get("damage_vulnerabilities") else None,
        "damage_resistances_id": monster_id if monster.get("damage_resistances") else None,
        "damage_immunities_id": monster_id if monster.get("damage_immunities") else None,
        "condition_immunities_id": monster_id if monster.get("condition_immunities") else None,
        "actions_id": monster_id if monster.get("actions") else None,
        "legendary_actions_id": monster_id if monster.get("legendary_actions") else None,
        "special_abilities_id": monster_id if monster.get("special_abilities") else None,
        "reactions_id": monster_id if monster.get("reactions") else None,
    }

    cur.execute(f"""
        UPDATE monsters SET
            proficiencies_id = %s,
            damage_vulnerabilities_id = %s,
            damage_resistances_id = %s,
            damage_immunities_id = %s,
            condition_immunities_id = %s,
            actions_id = %s,
            legendary_actions_id = %s,
            special_abilities_id = %s,
            reactions_id = %s
        WHERE id = %s
    """, (
        m2m_data["proficiencies_id"],
        m2m_data["damage_vulnerabilities_id"],
        m2m_data["damage_resistances_id"],
        m2m_data["damage_immunities_id"],
        m2m_data["condition_immunities_id"],
        m2m_data["actions_id"],
        m2m_data["legendary_actions_id"],
        m2m_data["special_abilities_id"],
        m2m_data["reactions_id"],
        monster_id
    ))

    print(f"✅ Eklendi: {name} (ID: {monster_id})")

conn.commit()
cur.close()
conn.close()
print("🎯 Tüm canavarlar başarıyla eklendi.")
