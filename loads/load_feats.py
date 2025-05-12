import json
from sqlalchemy import create_engine, text

# Veritabanı bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# Yardımcı fonksiyon: URL'den id çek
def get_id_by_url(conn, table_name, url):
    if not url:
        return None
    result = conn.execute(
        text(f"SELECT id FROM {table_name} WHERE url = :url"),
        {"url": url}
    ).fetchone()
    return result[0] if result else None

# JSON dosyasını yükle
with open("jsons/5e-SRD-Feats.json", "r", encoding="utf-8") as f:
    feats = json.load(f)

# Veritabanına veri ekle
with engine.begin() as conn:
    for feat in feats:
        prereq = feat.get("prerequisites", [])
        if prereq:
            ability_url = prereq[0].get("ability_score", {}).get("url")
            minimum_score = prereq[0].get("minimum_score")
        else:
            ability_url = None
            minimum_score = None

        ability_score_id = get_id_by_url(conn, "ability_scores", ability_url)

        conn.execute(text("""
            INSERT INTO feats (
                name, description, url, ability_score, minimum_score
            ) VALUES (
                :name, :description, :url, :ability_score, :minimum_score
            )
        """), {
            "name": feat.get("name"),
            "description": "\n".join(feat.get("desc", [])) if isinstance(feat.get("desc"), list) else feat.get("desc"),
            "url": feat.get("url"),
            "ability_score": ability_score_id,
            "minimum_score": minimum_score
        })

print("✅ Feats verileri başarıyla yüklendi.")
