from config import engine
from sqlalchemy.orm import Session
from models.all_models import Base as mainBase
from models.relation_models_full import Base as relationBase
from models.classes_fix_model import Base as clasesBase

if __name__ == "__main__":
    print("📦 Veritabanı tabloları oluşturuluyor...")
    mainBase.metadata.create_all(bind=engine)
    relationBase.metadata.create_all(bind=engine)
    clasesBase.metadata.create_all(bind=engine)
    print("✅ Tüm tablolar başarıyla oluşturuldu.")
