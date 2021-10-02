from boot import *

from ui.index import *

while True:
	option = printOptions("e-SHOP", MAIN_MENU)

	if option == 1:
		prf.saveAll(tds.getTestProducts())
		printItems(
			"Catalog of products", prf.all()
			)
		answer = input("Add to card? (y/n)")
		if answer == "y":
			prodoctId = int(input("enter product id: "))
			prodoct = prf.findById(prodoctId)
			print(prodoct)
		else:
			print("ok")
	if option == 2:
		print("Your cart")

	if option == 0:
		print("Thank you for using our app")
		break