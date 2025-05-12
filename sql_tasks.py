from sqlalchemy import create_engine, text

# Bağlantı bilgilerini kendi veritabanına göre ayarla
engine = create_engine("postgresql://postgres:postgres@localhost:5432/dnd_test")

with engine.connect() as conn:
    # 1. equipment_categories tablosundan "index" sütununu sil
    conn.execute(text("ALTER TABLE equipment_categories DROP COLUMN IF EXISTS index;"))
    print("✅ index sütunu silindi.")

    # 2. equipment tablosunun adını equipments olarak değiştir
    conn.execute(text("ALTER TABLE equipment RENAME TO equipments;"))
    print("✅ Tablo adı 'equipment' -> 'equipments' olarak değiştirildi.")

    # 3. id sütununu serial (auto increment) olarak ayarla
    conn.execute(text("ALTER TABLE equipments ALTER COLUMN id DROP DEFAULT;"))
    conn.execute(text("DROP SEQUENCE IF EXISTS equipments_id_seq;"))
    conn.execute(text("CREATE SEQUENCE equipments_id_seq START 1 OWNED BY equipments.id;"))
    conn.execute(text("ALTER TABLE equipments ALTER COLUMN id SET DEFAULT nextval('equipments_id_seq');"))
    print("✅ id sütunu artık SERIAL.")
