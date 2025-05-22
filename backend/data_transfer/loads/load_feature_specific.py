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
    # Tabloyu temizle ve ID sıfırla
    conn.execute(text("TRUNCATE TABLE feature_specific RESTART IDENTITY CASCADE"))

    for feature in features:
        fs = feature.get("feature_specific")
        url = feature.get("url")

        if not fs or not url:
            continue

        # URL ile eşleşen feature ID'sini al
        result = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": url})
        feature_id = result.scalar()
        if feature_id is None:
            continue

        # Başlangıç değerleri
        choose = fs.get("choose")
        description = fs.get("desc")
        enemy_type_options = None
        terrain_type_options = None
        invocation_id = None
        subfeature_id = None
        expertise_id = None

        # enemy_type_options içindekileri işle
        if "enemy_type_options" in fs:
            enemy = fs["enemy_type_options"]
            description = enemy.get("desc", description)
            if "from" in enemy and "options" in enemy["from"]:
                enemy_type_options = json.dumps(enemy["from"]["options"])
            if "choose" in enemy:
                choose = enemy["choose"]

        # terrain_type_options içindekileri işle
        if "terrain_type_options" in fs:
            terrain = fs["terrain_type_options"]
            description = terrain.get("desc", description)
            if "from" in terrain and "options" in terrain["from"]:
                terrain_type_options = json.dumps(terrain["from"]["options"])
            if "choose" in terrain:
                choose = terrain["choose"]

        # expertise_options içindekileri işle (choose'ü al, options loglanmaz)
        if "expertise_options" in fs:
            expertise = fs["expertise_options"]
            if "choose" in expertise:
                choose = expertise["choose"]

        # invocation, subfeature, expertise işaretçileri
        if "invocations" in fs:
            invocation_id = feature_id
        if "subfeature_options" in fs:
            subfeature_id = feature_id
        if "expertise_options" in fs:
            expertise_id = feature_id

        # INSERT işlemi
        conn.execute(text("""
            INSERT INTO feature_specific (
                feature_specific_id,
                description,
                enemy_type_options,
                choose,
                terrain_type_options,
                invocation_id,
                subfeature_id,
                expertise_id
            ) VALUES (
                :feature_specific_id,
                :description,
                :enemy_type_options,
                :choose,
                :terrain_type_options,
                :invocation_id,
                :subfeature_id,
                :expertise_id
            )
        """), {
            "feature_specific_id": feature_id,
            "description": description,
            "enemy_type_options": enemy_type_options,
            "choose": choose,
            "terrain_type_options": terrain_type_options,
            "invocation_id": invocation_id,
            "subfeature_id": subfeature_id,
            "expertise_id": expertise_id
        })

print("✅ feature_specific tablosu tüm choose alanları ve options içerikleriyle başarıyla dolduruldu.")
