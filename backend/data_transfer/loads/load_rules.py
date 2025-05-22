import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Rules.json"

# JSON verisini oku
with open(json_path, "r", encoding="utf-8") as f:
    rules_data = json.load(f)

# DB'ye yaz
with engine.begin() as conn:
    for rule in rules_data:
        name = rule.get("name")
        index = rule.get("index")
        description = rule.get("desc")
        url = rule.get("url")

        conn.execute(text("""
            INSERT INTO rules (name, index, description, url)
            VALUES (:name, :index, :description, :url)
        """), {
            "name": name,
            "index": index,
            "description": description,
            "url": url
        })

print("✅ Rules tablosu başarıyla yüklendi.")
