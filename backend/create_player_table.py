from sqlalchemy import create_engine
from models import Base

# FK verilen modeller (referans tablolar)
from models.models import (
    Classes,
    Subclasses,
    Races,
    Feats,
    Equipment,
    Spells,
    Skills,
    Languages,
    Traits,
    AbilityScores,
    Conditions
)

# Player tabanlı modeller (asıl tablolarımız)
from models.player import (
    User,
    Character,
    CharacterSpell,
    CharacterEquipment,
    CharacterSkill,
    CharacterLanguage,
    CharacterTrait,
    CharacterSavingThrow,
    CharacterCondition
)

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/dnd_test"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

print("✅ Kullanıcı ve karakter ile ilgili tüm tablolar oluşturuldu.")
