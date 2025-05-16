import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

def get_id_by_url(conn, table, url):
    if not url:
        return None
    result = conn.execute(
        text(f"SELECT id FROM {table} WHERE url = :url"),
        {"url": url}
    ).fetchone()
    return result[0] if result else None

# JSON dosyasını oku
with open("jsons/5e-SRD-Proficiencies.json", "r", encoding="utf-8") as f:
    proficiencies = json.load(f)

with engine.begin() as conn:
    for prof in proficiencies:
        ref_url = prof.get("reference", {}).get("url")
        url = prof.get("url")

        reference_equipment_id = None
        reference_equipment_category_id = None
        reference_skill_id = None
        reference_ability_score_id = None

        if ref_url:
            if "/api/2014/equipment/" in ref_url:
                reference_equipment_id = get_id_by_url(conn, "equipment", ref_url)
            elif "/api/2014/equipment-categories/" in ref_url:
                reference_equipment_category_id = get_id_by_url(conn, "equipment_categories", ref_url)
            elif "/api/2014/skills/" in ref_url:
                reference_skill_id = get_id_by_url(conn, "skills", ref_url)
            elif "/api/2014/ability-scores/" in ref_url:
                reference_ability_score_id = get_id_by_url(conn, "ability_scores", ref_url)

        conn.execute(text("""
            UPDATE proficiencies
            SET
                reference_equipment_id = :equipment_id,
                reference_equipment_category_id = :equipment_cat_id,
                reference_skill_id = :skill_id,
                reference_ability_score_id = :ability_score_id
            WHERE url = :url
        """), {
            "equipment_id": reference_equipment_id,
            "equipment_cat_id": reference_equipment_category_id,
            "skill_id": reference_skill_id,
            "ability_score_id": reference_ability_score_id,
            "url": url
        })

print("✅ Güncelleme tamamlandı: Skills ve Ability Scores dahil.")
