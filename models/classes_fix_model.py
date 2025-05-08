from sqlalchemy import Column, Integer, ForeignKey, Text
from models import Base

# 🔹 Class → Option (üst seviye bağlantı)
class ClassesStartingEquipmentOptions(Base):
    __tablename__ = 'classes_starting_equipment_options'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey("classes.id"))
    option_id = Column(Integer, ForeignKey("starting_equipment_option.id"))
    def __repr__(self): return f"<ClassesStartingEquipmentOptions {self.id}>"

# 🔹 Option Tanımı
class StartingEquipmentOption(Base):
    __tablename__ = 'starting_equipment_option'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    choose = Column(Integer)
    def __repr__(self): return f"<StartingEquipmentOption {self.id}>"

# 🔹 Option → OptionItem (birden fazla eşya içerebilir)
class StartingEquipmentOptionItem(Base):
    __tablename__ = 'starting_equipment_option_item'
    id = Column(Integer, primary_key=True)
    option_id = Column(Integer, ForeignKey("starting_equipment_option.id"))
    starting_equipment_id = Column(Integer, ForeignKey("starting_equipment.id"), nullable=True)  # 💥 asıl bağlantı bu!
    equipment_id = Column(Integer, ForeignKey("equipment.id"), nullable=True)
    equipment_category_id = Column(Integer, ForeignKey("equipment_categories.id"), nullable=True)
    quantity = Column(Integer, default=1)
    def __repr__(self): return f"<StartingEquipmentOptionItem {self.id}>"

# 🔹 Class → Direkt starting_equipment bağlantısı (options dışı sabit ekipmanlar için)
class ClassesStartingEquipment(Base):
    __tablename__ = 'classes_starting_equipment'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey("classes.id"))
    starting_equipment_id = Column(Integer, ForeignKey("starting_equipment.id"))
    def __repr__(self): return f"<ClassesStartingEquipment {self.id}>"
