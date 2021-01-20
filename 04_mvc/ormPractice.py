from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306/TESTDB')
Base = declarative_base()


class Staff(Base):
    __tablename__ = 'Staff'
    ID = Column(String(10), primary_key=True)
    Name = Column(String(45), nullable=False)
    DeptId = Column(String(10), nullable=False)
    Age = Column(Integer, default=None)
    Gender = Column(String(3), default=None)
    Salary = Column(Integer, default=None)
    RecordDt = Column(Date, nullable=False)

    def __repr__(self):
        return "<User(name='%s', record='%s'>" % (self.Name, self.RecordDt)


DBSession = sessionmaker(bind=engine)
session = DBSession()

for r in session.query(Staff):
    print(r)

session.commit()
session.close()
