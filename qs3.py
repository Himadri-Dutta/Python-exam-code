'''
Shopping Cart Management A customer adds products to a shopping cart.
 Write a function that accepts a list of product names and performs the following operations: 
• Add a new product. 
• Remove a purchased or unwanted product. 
• Display the final cart. 
• Count the total number of products. 

'''




prod = ['apple','banana','mango','cherry','berry']

def shop_cart(prod:list):
    print("You have added these products: ",prod)


def shop_cart_add(item:str):
    prod.append(item)


def shop_cart_remove(item:str):
    prod.remove(item)

def shop_cart_display():
    for _ in prod:
        print(_)


def shop_cart_count():
   print(len(prod))


shop_cart(prod)

shop_cart_count() 
shop_cart_add('litchi')
shop_cart_count() 
shop_cart_display()
shop_cart_remove('mango')
shop_cart_display()
shop_cart_count()
