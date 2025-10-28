import requests 
import json
# get---->read all products
url=('https://fakestoreapi.com/products')
# data=requests.get(url)
# print(data)
# for pro in data.json():
    # print(data.json())
    # print(pro["title"])

# 1.create data use method post:
product_data = {
    "title": "New Stylish Jacket",
    "price": 59.99,
    "description": "A trendy jacket for all seasons",
    "image": "https://example.com/jacket.png",
    "category": "men's clothing"
}
# post---->create a new product

# json_data=json.dumps(product_data)
# response = requests.post(url, json=product_data)
# print(response.json())

# put--->update the product

updated_data = {
    "title": "Stylish Winter Jacket",
    "price": 69.99,
    "description": "Updated version with warmer lining",
    "image": "https://example.com/jacket_new.png",
    "category": "men's clothing"
}

put_url = f"{url}/{new_id}"
response_put = requests.put(put_url, json=updated_data)
print("PUT - Update Product:")
print(response_put.json())
print("-" * 50)