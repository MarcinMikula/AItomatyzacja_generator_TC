# database/db_operations.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from TestCaseGenerator.database.db_setup import Requirement, TestCase
from TestCaseGenerator.config import DB_CONNECTION_STRING  # Poprawiony import

engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)

def add_test_case(requirement_id, name, prerequisites, steps, end_conditions, test_type):
    session = Session()
    test_case = TestCase(
        requirement_id=requirement_id,
        name=name,
        prerequisites=prerequisites,
        steps=steps,
        end_conditions=end_conditions,
        test_type=test_type
    )
    session.add(test_case)
    session.commit()
    session.close()