from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class product(Base):
   __tablename__ ='products'
   id = column(integer,primary_key=True)
   name = Column(String)
   price=column(Float)
   picture_link=column(String)
   description=column(String)
 class cart(base):
 	__tablename__='cart'
 	id = column(integer,primary_key=True)
 	productid = column(integer)
