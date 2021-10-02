import requests
from models.Product import Product
from models.Money import Money 

class TestDataService:
	def getTestProducts(self, count = 30):
		res = requests.get("https://fakestoreapi.com/products")
		Products = []
		if res.status_code == 200:
			data = res.json()
			for item in data:
				product = Product(item["id"], item["title"], Money(item["price"], "USD"))
				Products.append(product)
		else:
			raise Exception("Connection error!!!")
		return Products