MAIN_MENU = {
	1: "Catalog",
	2: "Cart",
	3: "Exit"
}

def printOptions(title, options):
	print(f"\n{title}")
	print("#"*50)

	for key in options:
		print(f"{key}, {options[key]}")

	print("#"*50)
	option = int(input(">> "))

	return option 

def printItems(title, items):
	print(f"\n{title}")
	print("#"*50)

	for key in items:
		print(f"{items}")

	print("#"*50)