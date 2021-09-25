import os

from sqlalchemy import Column, Integer, String

from config import Session, Base


class Job(Base):
    """ Job Model for storing user related details """
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    company_name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    date_from = Column(String(50), nullable=False)
    date_to = Column(String(50), nullable=True)
    job_type = Column(String(50), nullable=False)

    def __init__(self, company_name, description, date_from, job_type, date_to=''):
        self.company_name = company_name
        self.description = description
        self.date_from = date_from
        self.job_type = job_type
        self.date_to = date_to

    @staticmethod
    def get_all():
        session = Session()
        return session.query(Job).all()

    def save(self):
        session = Session()
        session.add(self)
        session.commit()
