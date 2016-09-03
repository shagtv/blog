#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class X(Base):
    __tablename__ = 'x'
    a = Column(Integer, primary_key=True)
    b = Column(Integer)

    def __str__(self):
        return '{} {} {}'.format(self.__class__.__name__, self.a, self.b)

    def __repr__(self):
        return '{} {} {}'.format(self.__class__.__name__, self.a, self.b)

engine = create_engine('sqlite:///tutorial6.db')
engine.echo = True

Session = sessionmaker(bind=engine)

#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)

s = Session()
#print('start')
#for i in range(1000000):
#    s.add(X(a=i, b=i))
#print('commit')
#s.commit()
#print('end')

def grouper(iterable, n):
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk

result = s.query(X).yield_per(500)
i = 0
for x in grouper(result, 500):
    i += 1
    #print(x)
print(i)
s.close()
