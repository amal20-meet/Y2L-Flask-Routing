from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def add_product(name,price,picture_link,description)
	product = product(
	product = session.query(name,price,picture_link,description).all
		name=name,
		price=price,
		picture_link=picture_link,
		description=description)
	session.add(product_object)
	session.commit()
add_product("mayuri",100,"5alas")
session.commit()

def edit_product(name,price,picture_link,description)
	product = product(
	name=name,
	price=price,
	picture_link=picture_link,
	description=description)
	session.query(product).filter_by(
       name=name)
	product.naaameeee=name,
	product.priceee=price,
	product.pictureee=picture_link,
	product.descriptionnn=description,
	session.commit()

def delete_productedit_product(id)
	session.query(product).filter_by(id=id).delete()
	session.commit()


	
def add_all():
	products = session.query(product).all()
	return(products) 
def add_by_id():
	product_id=session.query(product).filter_by(id=id)()
	session.commit()
	return(product_id)

   session.commit()
 def add_to_cart(productid):
 	productid_object = cart()
 	productid_object.productid = productid
 	session.add(productid_object)
 	session.commit()


		