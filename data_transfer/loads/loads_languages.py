import json
from sqlalchemy import create_engine, text

# DB bağlantısı
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

# JSON yolu
json_path = "/home/elovate/Desktop/dnd/jsons/5e-SRD-Languages.json"

# JSON yükle
with open(json_path, "r", encoding="utf-8") as f:
    langs = json.load(f)

with engine.begin() as conn:
    for lang in langs:
        name = lang.get("name")
        type_ = lang.get("type")
        script = lang.get("script")
        url = lang.get("url")
        typical_speakers = ", ".join(lang.get("typical_speakers", []))
        description = lang.get("desc")

        conn.execute(text("""
            INSERT INTO languages (name, type, script, url, typical_speakers, description)
            VALUES (:name, :type, :script, :url, :typical_speakers, :description)
        """), {
            "name": name,
            "type": type_,
            "script": script,
            "url": url,
            "typical_speakers": typical_speakers,
            "description": description
        })

print("✅ Languages başarıyla yüklendi.")
