import json
from sqlalchemy import create_engine, text

# Veritabanı bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# Yardımcı fonksiyon: belirli bir url ile id'yi eşleştir
def get_id_by_url(conn, table_name, url):
    if not url:
        return None
    result = conn.execute(
        text(f"SELECT id FROM {table_name} WHERE url = :url"),
        {"url": url}
    ).fetchone()
    return result[0] if result else None

# JSON verisini yükle
with open("jsons/5e-SRD-Equipment.json", "r", encoding="utf-8") as f:
    equipments = json.load(f)

# Veritabanına veri yükleme
with engine.begin() as conn:
    for item in equipments:
        # FK id'lerini url'ye göre eşleştir
        equipment_category_id = get_id_by_url(conn, "equipment_categories", item.get("equipment_category", {}).get("url"))
        gear_category_id = get_id_by_url(conn, "equipment_categories", item.get("gear_category", {}).get("url"))
        damage_type_id = get_id_by_url(conn, "damage_types", item.get("damage", {}).get("damage_type", {}).get("url"))
        two_handed_damage_type_id = get_id_by_url(conn, "damage_types", item.get("two_handed_damage", {}).get("damage_type", {}).get("url"))

        # Veriyi veritabanına ekle
        conn.execute(text("""
            INSERT INTO equipment (
                category_range, damage_dice, description,
                equipment_category, gear_category, name,
                range_normal, special, speed_quantity,
                stealth_disadvantage, str_minimum, throw_range_normal,
                tool_category, two_handed_damage_dice, url,
                vehicle_category, weight, weapon_category, weapon_range,
                cost_quantity, cost_unit, damage_type, range_long,
                speed_unit, two_handed_damage_type, throw_range_long
            ) VALUES (
                :category_range, :damage_dice, :description,
                :equipment_category, :gear_category, :name,
                :range_normal, :special, :speed_quantity,
                :stealth_disadvantage, :str_minimum, :throw_range_normal,
                :tool_category, :two_handed_damage_dice, :url,
                :vehicle_category, :weight, :weapon_category, :weapon_range,
                :cost_quantity, :cost_unit, :damage_type, :range_long,
                :speed_unit, :two_handed_damage_type, :throw_range_long
            )
        """), {
            "category_range": item.get("category_range"),
            "damage_dice": item.get("damage", {}).get("damage_dice"),
            "description": "\n".join(item.get("desc", [])) if isinstance(item.get("desc"), list) else item.get("desc"),
            "equipment_category": equipment_category_id,
            "gear_category": gear_category_id,
            "name": item.get("name"),
            "range_normal": item.get("range", {}).get("normal"),
            "special": "\n".join(item.get("special", [])) if isinstance(item.get("special"), list) else item.get("special"),
            "speed_quantity": item.get("speed", {}).get("quantity"),
            "stealth_disadvantage": item.get("stealth_disadvantage"),
            "str_minimum": item.get("str_minimum"),
            "throw_range_normal": item.get("throw_range", {}).get("normal"),
            "tool_category": item.get("tool_category"),
            "two_handed_damage_dice": item.get("two_handed_damage", {}).get("damage_dice"),
            "url": item.get("url"),
            "vehicle_category": item.get("vehicle_category"),
            "weight": item.get("weight"),
            "weapon_category": item.get("weapon_category"),
            "weapon_range": item.get("weapon_range"),
            "cost_quantity": item.get("cost", {}).get("quantity"),
            "cost_unit": item.get("cost", {}).get("unit"),
            "damage_type": damage_type_id,
            "range_long": item.get("range", {}).get("long"),
            "speed_unit": item.get("speed", {}).get("unit"),
            "two_handed_damage_type": two_handed_damage_type_id,
            "throw_range_long": item.get("throw_range", {}).get("long"),
        })

print("✅ Equipment verileri foreign key'lerle birlikte yüklendi.")
