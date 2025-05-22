import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Skills.json"

# JSON yükle
with open(json_path, "r", encoding="utf-8") as f:
    skills = json.load(f)

with engine.begin() as conn:
    for skill in skills:
        name = skill.get("name")
        description = "\n".join(skill.get("description", []))
        url = skill.get("url")

        # ability_score URL ile eşleşen ID'yi bul
        ability_score_url = skill.get("ability_score", {}).get("url")
        if not ability_score_url:
            continue

        result = conn.execute(
            text("SELECT id FROM ability_scores WHERE url = :url"),
            {"url": ability_score_url}
        ).fetchone()

        if not result:
            print(f"[!] Eşleşme bulunamadı: {ability_score_url}")
            continue

        ability_score_id = result[0]

        conn.execute(text("""
            INSERT INTO skills (name, description, ability_score, url)
            VALUES (:name, :description, :ability_score, :url)
        """), {
            "name": name,
            "description": description,
            "ability_score": ability_score_id,
            "url": url
        })

print("✅ Skills başarıyla yüklendi.")
