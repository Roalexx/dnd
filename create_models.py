from config import engine
from sqlalchemy.orm import Session
from models.features_prerequisites_model import Base

if __name__ == "__main__":
    print("📦 Veritabanı tabloları oluşturuluyor...")
    Base.metadata.create_all(bind=engine)
 
    print("✅ Tüm tablolar başarıyla oluşturuldu.")
