import json
from sqlalchemy import create_engine, text

# Veritabanı bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosyası
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Rules.json"

with open(json_path, "r", encoding="utf-8") as f:
    rules_data = json.load(f)

with engine.begin() as conn:
    for rule in rules_data:
        rule_url = rule.get("url")
        subsections = rule.get("subsections", [])

        # 1. rules tablosundan ID'yi bul
        rule_id = conn.execute(text("""
            SELECT id FROM rules WHERE url = :url
        """), {"url": rule_url}).scalar()

        if not rule_id:
            print(f"[!] Rule bulunamadı: {rule_url}")
            continue

        # 2. Her subsection için eşleşen rule_sections id'sini bul ve ekle
        for subsection in subsections:
            section_url = subsection.get("url")
            section_id = conn.execute(text("""
                SELECT id FROM rule_sections WHERE url = :url
            """), {"url": section_url}).scalar()

            if not section_id:
                print(f"[!] Rule Section bulunamadı: {section_url}")
                continue

            # 3. Eşleşmeyi insert et
            conn.execute(text("""
                INSERT INTO rules_subsections (rules_id, rule_sections_id)
                VALUES (:rule_id, :section_id)
            """), {
                "rule_id": rule_id,
                "section_id": section_id
            })

print("✅ rules_subsections tablosu başarıyla dolduruldu.")
