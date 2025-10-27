# ecommerce_data = [
#     {"id": 1, "name": "iPhone 15", "category": "Electronics", "price": 79999, "stock": 25},
#     {"id": 2, "name": "Nike Air Max", "category": "Fashion", "price": 8999, "stock": 50},
#     {"id": 3, "name": "Organic Almonds 1kg", "category": "Grocery", "price": 1200, "stock": 100},
#     {"id": 4, "name": "Samsung 55-inch 4K TV", "category": "Electronics", "price": 54999, "stock": 15},
#     {"id": 5, "name": "Wooden Dining Table", "category": "Furniture", "price": 25999, "stock": 10},
#     {"id": 6, "name": "Sony WH-1000XM5 Headphones", "category": "Electronics", "price": 29990, "stock": 35},
#     {"id": 7, "name": "Adidas Hoodie", "category": "Fashion", "price": 4999, "stock": 60},
#     {"id": 8, "name": "Dettol Hand Wash (Pack of 3)", "category": "Health & Hygiene", "price": 299, "stock": 200},
#     {"id": 9, "name": "Harry Potter Box Set", "category": "Books", "price": 3499, "stock": 40},
#     {"id": 10, "name": "Lenovo IdeaPad Laptop", "category": "Computers", "price": 42999, "stock": 20}
# ]
# f_op=list(filter(lambda x:x['price']>=3000 and x['price']<=50000,ecommerce_data))
# print(f_op)


from functools import reduce
ip=['I','LOVE','INDIA']
OP=reduce(lambda x,y:x if len(x)<len(y) else y,ip)
print(OP)
OP=reduce(lambda x,y:x if len(x)>len(y) else y,ip)
print(OP)

OP=reduce(lambda x,y:x+y,ip)
print(OP)

ip1=[4,6,3,2,9]
op1=reduce(lambda x,y:x*10+y,ip1)
print(op1)