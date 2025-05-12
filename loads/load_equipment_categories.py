from sqlalchemy import create_engine, text
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "../jsons/5e-SRD-Equipment-Categories.json")

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

with open(json_path, "r", encoding="utf-8") as f:
    categories = json.load(f)

with engine.begin() as conn:  # önemli! BEGIN BLOĞU
    for cat in categories:
        name = cat.get("name")
        url = cat.get("url")
        if name and url:
            conn.execute(
                text("INSERT INTO equipment_categories (name, url) VALUES (:name, :url)"),
                {"name": name, "url": url}
            )

print("✅ Yükleme tamamlandı.")
