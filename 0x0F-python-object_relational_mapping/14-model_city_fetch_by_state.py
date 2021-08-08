#!/usr/bin/python3
"""Module lists State objects"""
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State, City).order_by(City.id)
    for x, j in states.all():
        print("{}: {} {}".format(x.name, j.id, j.name))
    session.close()
