import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON dosya yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Alignments.json"

# JSON verisini yükle
with open(json_path, "r", encoding="utf-8") as f:
    alignments = json.load(f)

with engine.begin() as conn:
    for aln in alignments:
        name = aln.get("name")
        description = aln.get("desc")
        url = aln.get("url")

        conn.execute(text("""
            INSERT INTO alignments (name, description, url)
            VALUES (:name, :description, :url)
        """), {
            "name": name,
            "description": description,
            "url": url
        })

print("✅ Alignments başarıyla yüklendi.")
