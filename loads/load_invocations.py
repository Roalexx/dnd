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
    # Tabloyu sıfırla
    conn.execute(text("TRUNCATE TABLE invocations RESTART IDENTITY CASCADE"))

    for feature in features:
        fs = feature.get("feature_specific")
        url = feature.get("url")

        if not fs or "invocations" not in fs or not url:
            continue

        # 1. features tablosundan feature.id alınır
        result = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": url})
        feature_id_fk = result.scalar()
        if feature_id_fk is None:
            continue

        # 2. feature_specific tablosundan invocation_id alınır (feature_specific.invocation_id)
        result2 = conn.execute(text("SELECT invocation_id FROM feature_specific WHERE feature_specific_id = :fid"), {"fid": feature_id_fk})
        invocation_id = result2.scalar()
        if invocation_id is None:
            continue  # invocation_id atanmadıysa geç

        # 3. her invocation.url için feature_id bulunup eklenir
        for invocation in fs["invocations"]:
            invoked_url = invocation.get("url")
            if not invoked_url:
                continue

            result3 = conn.execute(text("SELECT id FROM features WHERE url = :url"), {"url": invoked_url})
            target_feature_id = result3.scalar()
            if target_feature_id is None:
                continue

            # 4. INSERT işlemi
            conn.execute(text("""
                INSERT INTO invocations (invocation_id, feature_id)
                VALUES (:invocation_id, :feature_id)
            """), {
                "invocation_id": invocation_id,
                "feature_id": target_feature_id
            })

print("✅ invocations tablosu DOĞRU invocation_id eşleşmesiyle başarıyla dolduruldu.")
