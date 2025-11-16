import requests 
import json
# 1.get---->read all products
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
# 2. post---->create a new product

json_data=json.dumps(product_data)
response = requests.post(url, json=product_data)
print(response.json())

new_id = response.json().get("id", 21)
# 3. put--->update the product

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

# 4.DELETE – Remove the product
delete_url = f"{url}/{new_id}"
response_delete = requests.delete(delete_url)
print("DELETE - Product Removed:")
if response_delete.text.strip():   
    print(response_delete.json())
else:
    print("No content returned (status code:", response_delete.status_code, ")")

print("-" * 50)



# ------------------------------------------------------------------------------------------------------
# api
import requests
import json

url = "https://fakestoreapi.com/products"

#  Header (tells server we are sending JSON)
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

body = {
    "title": "Smart Watch",
    "price": 199.99,
    "description": "A stylish smartwatch with fitness tracking",
    "image": "https://example.com/watch.png",
    "category": "electronics"
}
url = "https://fakestoreapi.com/products"
headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print("GET Response:", response.json()[:2])
update_url = "https://fakestoreapi.com/products/1"

headers = {
    "Content-Type": "application/json"
}

update_body = {
    "title": "Updated Product Title",
    "price": 249.99
}

response = requests.put(update_url, headers=headers, json=update_body)
print("PUT Response:", response.json())
















