from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class FeaturePrerequisite(Base):
    __tablename__ = 'feature_prerequisites'

    id = Column(Integer, primary_key=True)
    
    feature_id = Column(Integer, ForeignKey('features.prerequisites_id'), nullable=False)
    prerequisites_feature_id = Column(Integer, ForeignKey('features.prerequisites_id'), nullable=True)
    prerequisites_spell_id = Column(Integer, ForeignKey('spells.id'), nullable=True)

    def __repr__(self):
        return f"<FeaturePrerequisite {self.id}>"