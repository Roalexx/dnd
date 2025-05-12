import json
from sqlalchemy import create_engine, text

# Veritabanı bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Magic-Items.json"

# Dosyayı aç
with open(json_path, "r", encoding="utf-8") as f:
    items = json.load(f)

with engine.begin() as conn:
    for item in items:
        # 🔥 1. "variant" varsa ve boş değilse geç
        if "variant" in item and item["variant"]:
            continue

        name = item.get("name")
        desc = item.get("desc")
        rarity = item.get("rarity", {}).get("name")
        url = item.get("url")

        # 🔍 equipment_category içindeki url ile id bul
        eq_cat_url = item.get("equipment_category", {}).get("url")
        if not eq_cat_url:
            continue  # yoksa geç

        result = conn.execute(
            text("SELECT id FROM equipment_categories WHERE url = :url"),
            {"url": eq_cat_url}
        ).fetchone()

        if not result:
            print(f"[!] Eşleşme bulunamadı: {eq_cat_url}")
            continue

        equipment_category_id = result[0]

        # ✅ magic_items tablosuna ekle
        conn.execute(text("""
            INSERT INTO magic_items (name, description, rarity, url, equipment_category)
            VALUES (:name, :description, :rarity, :url, :equipment_category)
        """), {
            "name": name,
            "description": desc,
            "rarity": rarity,
            "url": url,
            "equipment_category": equipment_category_id
        })

print("✅ Magic items yükleme tamamlandı (variant olmayanlar).")
