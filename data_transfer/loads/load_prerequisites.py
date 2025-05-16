import json
from sqlalchemy import create_engine, text

# PostgreSQL bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Features.json"

# JSON'u yükle
with open(json_path, "r", encoding="utf-8") as f:
    features = json.load(f)

with engine.begin() as conn:
    # tabloyu tamamen temizle + ID sıfırla
    conn.execute(text("TRUNCATE TABLE prerequisites RESTART IDENTITY CASCADE"))

    for feature in features:
        prereqs = feature.get("prerequisites", [])
        if not prereqs:
            continue

        # features.url → features.id (prerequisites_id)
        feature_url = feature.get("url")
        result = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": feature_url})
        feature_id_fk = result.scalar()
        if feature_id_fk is None:
            continue

        for prereq in prereqs:
            if prereq.get("type") == "level":
                continue  # level olanları geç

            # spell ve feature hem dict hem string olabilir
            raw_spell = prereq.get("spell")
            raw_feat = prereq.get("feature")

            spell_url = raw_spell.get("url") if isinstance(raw_spell, dict) else raw_spell if isinstance(raw_spell, str) else None
            feature_url_ = raw_feat.get("url") if isinstance(raw_feat, dict) else raw_feat if isinstance(raw_feat, str) else None

            spell_id = None
            feature_prereq_id = None

            if spell_url:
                res = conn.execute(text("SELECT id FROM spells WHERE url = :url"), {"url": spell_url})
                spell_id = res.scalar()

            if feature_url_:
                res = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": feature_url_})
                feature_prereq_id = res.scalar()

            # en az bir eşleşme varsa ekle
            if spell_id or feature_prereq_id:
                conn.execute(text("""
                    INSERT INTO prerequisites (prerequisites_id, spell_id, feature_id)
                    VALUES (:prerequisites_id, :spell_id, :feature_id)
                """), {
                    "prerequisites_id": feature_id_fk,
                    "spell_id": spell_id,
                    "feature_id": feature_prereq_id
                })

print("✅ prerequisites tablosu temizlendi ve yeniden dolduruldu (spell + feature uyumlu).")
