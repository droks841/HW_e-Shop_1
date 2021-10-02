from services.TestDataService import *
from services.JSONDataService import *
from models.Product import *
from models.Order import *
from models.OrderItem import *

prf = ProductRepositoryFactory()
orf = OrderRepositoryFactory()
oirf = OrderItemRepositoryFactory()

prf = ProductRepositoryFactory()
tds = TestDataService()
jds = JSONDataService()