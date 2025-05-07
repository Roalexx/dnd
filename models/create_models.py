from config import engine
from models.relation_table_models import Base  # tüm modellerin Base'i burada

Base.metadata.create_all(bind=engine)
