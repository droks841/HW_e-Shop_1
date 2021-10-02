from .Money import *
class Product:
	def __init__(self, id, image_path, name, price):
		self.id = id
		self.image_path = image_path
		self.name = name
		self.setPrice( price )

	def setPrice(self, price):
		if type(price) != Money:
			raise typeError("Price must be of type Money!")
		if price.amount < 0:	
			raise ValueError("Product's price cannot be negative!")
		self._price = price

	def getPrice(self):
		return self._price 

	def __str__(self):
		return f"\n " \
			   f"Product ID: {self.id}\n " \
			   f"Name: {self.name}\n " \
			   f"price: {self._price}\n "

	def __repr__(self):
		return str(self)

class ProductRepositoryFactory:
	def __init__(self):
		self.lastCreatedId = 0
		self._products = []

	def getProduct(self, image_path, name, price):
		obj = Product(id, image_path, name, price)
		self.lastCreatedId += 1
		obj.id = self.lastCreatedId

		self.save(obj)

		return obj

	def save(self, product):
		self._products.append( product )

	def saveAll(self, products):
		self._products = products

	def all(self):
		return tuple(self._products)

	def findById(self, id):

		for p in self._products:
			if p.id == id:
				return p