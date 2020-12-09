from sqlalchemy import create_engine, Column, Integer, Boolean, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("postgresql://postgres:qwerty@localhost/test")

Session = sessionmaker(bind=engine)

session = Session()

class Parking(Base):
    __tablename__ = "parking"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    occupied = Column(Boolean)

    def __repr__(self):
        return f"<Parking(id={self.id}, occupied={self.occupied})>"


# import psycopg2

# conn = psycopg2.connect(dbname="test", user="postgres", password="qwerty", host='localhost', port=5432)

# cursor = conn.cursor()

# cursor.execute("select * from parking")

# data = cursor.fetchall()

# # print(data)