#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessio


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}\
            @localhost/{dbname}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=eng)
    session = Session()

    for state in session.query(state).order_by(state.id):
        print('{}: {}'.format(state.id, state.name))
    session.close()
