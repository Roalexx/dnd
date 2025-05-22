import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Spells.json", "r", encoding="utf-8") as f:
    spells_data = json.load(f)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Yardımcı: URL'den ID çek
def get_id_by_url(table, url):
    cur.execute(f"SELECT id FROM {table} WHERE url = %s", (url,))
    result = cur.fetchone()
    return result[0] if result else None

# Her büyü için güncelleme yap
for i, spell in enumerate(spells_data):
    spell_id = i + 1

    # dc_id için doğru URL eşlemesi
    dc_id = get_id_by_url("ability_scores", spell["dc"]["dc_type"]["url"]) if "dc" in spell else None

    # Diğer eşleştirmeler
    school_id = get_id_by_url("magic_schools", spell["school"]["url"]) if "school" in spell else None
    damage_type_id = get_id_by_url("damage_types", spell.get("damage", {}).get("damage_type", {}).get("url")) if "damage" in spell else None

    # Class ve Subclass eşlemeleri
    classes_id = spell_id if spell.get("classes") else None
    subclasses_id = spell_id if spell.get("subclasses") else None

    # damage_at_slot_level formatını düzelt
    damage_at_slot_level = None
    if "damage" in spell and "damage_at_slot_level" in spell["damage"]:
        damage_at_slot_level = ",".join(
            [f"level {lvl}:{val}" for lvl, val in spell["damage"]["damage_at_slot_level"].items()]
        )

    heal_at_slot_level = None
    if "heal_at_slot_level" in spell:
        heal_at_slot_level = ",".join(
            [f"level {lvl}:{val}" for lvl, val in spell["heal_at_slot_level"].items()]
        )

    # Area of effect
    area_type = spell.get("area_of_effect", {}).get("type")
    area_size = spell.get("area_of_effect", {}).get("size")

    attack_type = spell.get("attack_type")
    casting_time = spell.get("casting_time")
    components = ", ".join(spell.get("components", [])) if spell.get("components") else None
    concentration = spell.get("concentration")
    desc = "\n\n".join(spell.get("desc", [])) if spell.get("desc") else None
    duration = spell.get("duration")
    higher_level = "\n\n".join(spell.get("higher_level", [])) if spell.get("higher_level") else None
    level = spell.get("level")
    material = spell.get("material")
    range_ = spell.get("range")
    saving_throw = spell.get("dc", {}).get("dc_success") if "dc" in spell else None

    # Veritabanı güncelleme
    cur.execute("""
        UPDATE spells
        SET
            school_id = %s,
            dc_id = %s,
            damage_type_id = %s,
            classes_id = %s,
            subclasses_id = %s,
            damage_at_slot_level = %s,
            heal_at_slot_level = %s,
            area_of_effect_type = %s,
            area_of_effect_size = %s,
            attack_type = %s,
            casting_time = %s,
            components = %s,
            concentration = %s,
            description = %s,
            duration = %s,
            higher_level = %s,
            level = %s,
            material = %s,
            "range" = %s,
            saving_throw = %s
        WHERE id = %s
    """, (
        school_id,
        dc_id,
        damage_type_id,
        classes_id,
        subclasses_id,
        damage_at_slot_level,
        heal_at_slot_level,
        area_type,
        area_size,
        attack_type,
        casting_time,
        components,
        concentration,
        desc,
        duration,
        higher_level,
        level,
        material,
        range_,
        saving_throw,
        spell_id
    ))

# Commit ve bağlantıyı kapat
conn.commit()
cur.close()
conn.close()
