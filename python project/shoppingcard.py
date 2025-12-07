
products = [ 
{"id": 1, "name": "Laptop", "price": 45000}, 
{"id": 2, "name": "Smartphone", "price": 15000}, 
{"id": 3, "name": "Headphones", "price": 2000}, 
{"id": 4, "name": "Keyboard", "price": 1200}, 
{"id": 5, "name": "Mouse", "price": 800}, 
{"id": 6, "name": "Charger", "price": 500}, 
{"id": 7, "name": "USB Cable", "price": 300}, 
{"id": 8, "name": "Backpack", "price": 2500} 
] 

cart=[]

def view_products(products):
    print("\n--------Available Products--------")
    for product in products:
        print(f"The product name is {product['name']} and price is {product['price']}")
        print("----------------------")
    menu()
    
def add_to_cart(products,cart,product_id,quantity):
    product=None
    for items in products:
        if items['id']==product_id:
            product=items
            break
        if not product:
            print("the cart is empty")
    for item in cart:
        if item['id']==product_id:
            item['quantity']+=quantity
            print(f"Updated quantity for {item['name']} to {item['quantity']}")
    new_item={
        'id':product['id'],
        'name':product['name'],
        'price':product['price']*quantity,
        'quantity':quantity
        
    }
    cart.append(new_item)
    print(f"{product['name']} added to cart!")
    view_cart(cart)
    menu()
    

def view_cart(cart):
    if not cart:
        print("your cart is empty!")
    print("\n--------Your Shopping Cart--------")
    for items in cart:
        print(items)
    menu()

def update_cart(cart,product_id,quantity):
    for item in cart:
        if item['id']==product_id:
            item['quantity']=quantity
            print("item quentity updated sucessfully")
            break
    else:
        print("Product Not Found")
    menu()

def remove_from_cart(cart,product_id):
    found=False
    for item in cart:
        if item['id']==product_id:
            cart.remove(item)
            print(f"{item['name']} is removed from the cart")
            found=True
            break
    if not found:
        print("Product Not Found in cart")
    menu()

def checkout(cart):
    if not cart:
        print("your cart is empty! Add something first.")
    total=0
    for item in cart:
        subtotal=item['price']*item['quantity']
        total+=subtotal
        print(f"{item['name']}-{item['price']}x{item['quantity']}={subtotal}")
        print(f"Total bill:{total}")




def menu():
    # while True:
        print("""
--------Shopping Cart--------
              1.View Products
              2.Add to Cart
              3.View Cart
              4.Update Cart
              5.Remove from Cart
              6.Checkout
              7.Exit
              """)
        try:
             choice=int(input("enter your choice:"))
        except ValueError:
             print("please enter a valid number!")
        if choice==1:
            view_products(products)
        elif choice==2:
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            add_to_cart(products,cart,product_id,quantity)
        elif choice==3:
            view_cart(cart)
        elif choice==4:
            product_id = int(input("Enter Product ID to update: "))
            quantity = int(input("Enter new Quantity: "))
            update_cart(cart,product_id,quantity)
        elif choice==5:
            product_id=int(input("Enter Product ID to remove:"))
            remove_from_cart(cart,product_id)
        elif choice==6:
            checkout(cart)
        elif choice==7:
            print("Exiting Program.")
        else:
            print("invalid choice")
menu()