# database/db_setup.py
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from TestCaseGenerator.config import DB_CONNECTION_STRING  # Absolutny import

# Tworzenie bazy danych
engine = create_engine(DB_CONNECTION_STRING, echo=True)
Base = declarative_base()

# Tabela wymagań
class Requirement(Base):
    __tablename__ = "requirements"
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    priority = Column(String(20), default="Medium")
    test_cases = relationship("TestCase", back_populates="requirement")

# Tabela przypadków testowych
class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(Integer, primary_key=True)
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    name = Column(String(100), nullable=False)
    prerequisites = Column(Text)
    steps = Column(Text)
    end_conditions = Column(Text)
    test_type = Column(String(50))
    requirement = relationship("Requirement", back_populates="test_cases")

# Tworzenie tabel w bazie danych
def create_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_database()
    print("Baza danych i tabele zostały utworzone.")