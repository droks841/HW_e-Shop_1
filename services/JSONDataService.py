import json
from models.Product import Product
from models.Money import Money 

class JSONDataService:
	def getProducts(self, count = 20):
		Products = []
		data = json.load(open("data/products.json"))
		for item in data:
			product = Product(item["id"], item["image"], item["title"], Money(item["price"], "USD"))
			Products.append(product)
		return Products
