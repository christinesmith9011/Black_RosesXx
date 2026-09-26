sale=input('Would you like a muffin or cupcake?')
muffin = 10
cupcake = 10

while sale != "0":
    if sale == "muffin" and muffin >0:
             muffin = muffin -1
             print("muffin out of stock")
    if sale == "cupcake" and cupcake >0:
        cupcake = cupcake -1
        print("cupcake out of stock")
        sale=input('Would you like a muffin or cupcake?')

print("muffin:", muffin, "cupcake:", cupcake)
        
        
    
