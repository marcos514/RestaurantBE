import os

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config import Session, Base
from models.knowledge import Knowledge


association_table = Table('project_knowledges', Base.metadata,
    Column('knowledge_id', Integer, ForeignKey('knowledges.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)


class Project(Base):
    """ Project Model for storing user related details """
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    date_started = Column(String(50), nullable=False)
    date_finished = Column(String(50), nullable=True)
    status = Column(String(50), nullable=True)
    percentage_done = Column(Integer, nullable=True)
    knowledges = relationship("Knowledge", secondary=association_table, backref="project")

    def __init__(self, name, description, date_started, percentage_done, status, knowledges_id=[], date_finished=None):
        self.name = name
        self.description = description
        self.date_started = date_started
        self.date_finished = date_finished
        self.percentage_done = percentage_done
        self.status = status
        for knowledge_id in knowledges_id:
            knowledge = Knowledge.get_knowledge_by_id(knowledge_id)
            if knowledge:
                self.knowledges.append(knowledge)

    @staticmethod
    def get_all():
        session = Session()
        return session.query(Project).all()

    def save(self):
        session = Session()
        session.add(self)
        session.commit()
