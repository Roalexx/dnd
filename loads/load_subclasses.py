# load_subclasses.py
import json
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

with open("jsons/5e-SRD-Subclasses.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with engine.begin() as conn:
    for item in data:
        conn.execute(
            text("INSERT INTO subclasses (name, url) VALUES (:name, :url)"),
            {"name": item["name"], "url": item["url"]}
        )

print("✅ Subclasses tablosu yüklendi.")
