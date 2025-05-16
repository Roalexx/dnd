import psycopg2

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="dnd_test",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Tüm classes ve levels verisini al
cur.execute("SELECT id, name FROM classes")
classes = cur.fetchall()

cur.execute("SELECT id, url FROM levels")
levels = cur.fetchall()

inserted = 0

for class_id, class_name in classes:
    class_name_lower = class_name.lower()
    for level_id, level_url in levels:
        if class_name_lower in level_url.lower():
            cur.execute("""
                INSERT INTO classes_levels (class_id, level_id)
                VALUES (%s, %s)
            """, (class_id, level_id))
            inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"🎯 {inserted} classes_levels kaydı başarıyla eklendi.")
