#!/usr/bin/python3
"""Module lists State objects"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(text("id='{}'".format(2)))
    state = states.first()
    if state is None:
        print('Not found')
    else:
        state.name = 'New Mexico'
        session.commit()
    session.close()
