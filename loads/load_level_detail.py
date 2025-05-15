import json
import psycopg2

# JSON dosyasını yükle
with open("jsons/5e-SRD-Levels.json", "r", encoding="utf-8") as f:
    levels_data = json.load(f)

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# TABLOYU TEMİZLE (güvenli çalıştırmak için)
cur.execute("TRUNCATE TABLE level_detail RESTART IDENTITY CASCADE;")

# Veri yükleme
for entry in levels_data:
    sc = entry.get("spellcasting", {})
    cs = entry.get("class_specific", {})
    ss = entry.get("subclass_specific", {})
    features = entry.get("features", [])
    has_features = len(features) > 0

    # Önce detail'ı INSERT et
    cur.execute("""
        INSERT INTO level_detail (
            cantrips_known, spells_known,
            spell_slots_level_1, spell_slots_level_2, spell_slots_level_3,
            spell_slots_level_4, spell_slots_level_5, spell_slots_level_6,
            spell_slots_level_7, spell_slots_level_8, spell_slots_level_9,

            rage_count, rage_damage_bonus, brutal_critical_dice,
            bardic_inspiration_die, song_of_rest_die,
            magical_secrets_max_5, magical_secrets_max_7, magical_secrets_max_9,
            wild_shape_max_cr, wild_shape_swim, wild_shape_fly,
            extra_attacks, action_surges, indomitable_uses,
            channel_divinity_charges, destroy_undead_cr,
            additional_magical_secrets_max_lvl,
            features_id
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        sc.get("cantrips_known"), sc.get("spells_known"),
        sc.get("spell_slots_level_1"), sc.get("spell_slots_level_2"), sc.get("spell_slots_level_3"),
        sc.get("spell_slots_level_4"), sc.get("spell_slots_level_5"), sc.get("spell_slots_level_6"),
        sc.get("spell_slots_level_7"), sc.get("spell_slots_level_8"), sc.get("spell_slots_level_9"),

        cs.get("rage_count"), cs.get("rage_damage_bonus"), cs.get("brutal_critical_dice"),
        cs.get("bardic_inspiration_die"), cs.get("song_of_rest_die"),
        cs.get("magical_secrets_max_5"), cs.get("magical_secrets_max_7"), cs.get("magical_secrets_max_9"),
        cs.get("wild_shape_max_cr"), cs.get("wild_shape_swim"), cs.get("wild_shape_fly"),
        cs.get("extra_attacks"), cs.get("action_surges"), cs.get("indomitable_uses"),
        cs.get("channel_divinity_charges"), cs.get("destroy_undead_cr"),
        ss.get("additional_magical_secrets_max_lvl"),
        None  # geçici olarak NULL
    ))

    detail_id = cur.fetchone()[0]

    # Eğer features varsa, kendi ID'sini features_id olarak set et
    if has_features:
        cur.execute("""
            UPDATE level_detail
            SET features_id = %s
            WHERE id = %s
        """, (detail_id, detail_id))

# Değişiklikleri kaydet
conn.commit()
cur.close()
conn.close()
