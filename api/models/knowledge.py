import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config import Session, Base



class Knowledge(Base):
    """ Knowledge Model for storing user related details """
    __tablename__ = "knowledges"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    level = Column(Integer, nullable=False)
    parent_knowledge = Column(Integer, ForeignKey('knowledges.id'), nullable=True)
    child_knowledges = relationship("Knowledge")

    def __init__(self, name, level, parent_knowledge=None):
        self.name = name
        self.level = level
        self.parent_knowledge = parent_knowledge

    @staticmethod
    def get_all():
        session = Session()
        
        return session.query(Knowledge).filter_by(parent_knowledge=None).order_by(Knowledge.level.desc()).all()

    def save(self):
        session = Session()
        session.add(self)
        session.commit()

    @staticmethod
    def get_knowledge_by_id(id):
        session = Session()
        return session.query(Knowledge).filter_by(id=id).one()