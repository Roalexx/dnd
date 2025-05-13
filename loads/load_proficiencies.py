import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

def get_reference_data(conn, url):
    if not url:
        return None, None

    if "/equipment-categories/" in url:
        table = "equipment_categories"
        ref_type = "equipment_categories"
    elif "/equipment/" in url:
        table = "equipment"
        ref_type = "equipment"
    elif "/skills/" in url:
        table = "skills"
        ref_type = "skills"
    elif "/ability-scores/" in url:
        table = "ability_scores"
        ref_type = "ability_scores"
    else:
        return None, None

    result = conn.execute(
        text(f"SELECT id FROM {table} WHERE url = :url"),
        {"url": url}
    ).fetchone()

    return (result[0], ref_type) if result else (None, None)

with open("jsons/5e-SRD-Proficiencies.json", "r", encoding="utf-8") as f:
    proficiencies = json.load(f)

with engine.begin() as conn:
    for item in proficiencies:
        ref_url = item.get("reference", {}).get("url")
        ref_id, ref_type = get_reference_data(conn, ref_url)

        conn.execute(text("""
            INSERT INTO proficiencies (name, type, url, reference_id, reference_type)
            VALUES (:name, :type, :url, :reference_id, :reference_type)
        """), {
            "name": item.get("name"),
            "type": item.get("type"),
            "url": item.get("url"),
            "reference_id": ref_id,
            "reference_type": ref_type
        })

print("✅ Proficiencies başarıyla yüklendi.")
