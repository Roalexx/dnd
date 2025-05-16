import json
from sqlalchemy import create_engine, text

# Veritabanı bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

def get_id_by_url(conn, table_name, url):
    if not url:
        return None
    result = conn.execute(
        text(f"SELECT id FROM {table_name} WHERE url = :url"),
        {"url": url}
    ).fetchone()
    return result[0] if result else None

# JSON yükle
with open("jsons/5e-SRD-Equipment.json", "r", encoding="utf-8") as f:
    equipments = json.load(f)

with engine.begin() as conn:
    for equipment in equipments:
        equipment_url = equipment.get("url")
        equipment_id = get_id_by_url(conn, "equipment", equipment_url)

        for prop in equipment.get("properties", []):
            weapon_prop_url = prop.get("url")
            weapon_prop_id = get_id_by_url(conn, "weapon_properties", weapon_prop_url)

            if equipment_id and weapon_prop_id:
                conn.execute(
                    text("""
                        INSERT INTO equipment_properties (equipment_id, weapon_properties_id)
                        VALUES (:equipment_id, :weapon_properties_id)
                    """),
                    {"equipment_id": equipment_id, "weapon_properties_id": weapon_prop_id}
                )

print("✅ Equipment-property ilişkileri yüklendi.")