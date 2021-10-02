from boot import *
import tkinter as tk 

images = []

def addToCart():
	pass

def randerCatalog():
	global images
	global window
	prf.saveAll(jds.getProducts())
	products = prf.all()

	row = 1
	for product in products:
		img = tk.PhotoImage(file=product.image_path)
		images.append(img)
		lName = tk.Label(window, image=img, text=product.name)
		lName.grid(row = row, column = 0)

		lPrice = tk.Label(window, text=product.getPrice())
		lPrice.grid(row = row, column = 1)
		
		btnAdd2Cart = tk.Button(window, text="Buy", command=addToCart)
		btnAdd2Cart.grid(row = row, column = 2)
		row += 1

def randerCart():
	print("cart!")

window = tk.Tk()

menubar = tk.Menu(window)
menubar.add_command(label="Catalog", command=randerCatalog)
menubar.add_command(label="Cart", command=randerCart)

window.config(menu=menubar)
window.mainloop()