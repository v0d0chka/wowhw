import requests

url = "https://dummyjson.com/products?limit=200"
response = requests.get(url)

if response.status_code == 200:
    products = response.json()['products']
else:
    print("Error fetching data.")
    products = []

techgear_ids = [
    product['id'] for product in products if product.get('brand') == 'TechGear'
]
print("TechGear Product IDs:", techgear_ids)

product_135 = next((product for product in products if product['id'] == 135), None)
if product_135:
    image_url = product_135.get('image')
    if image_url:
        img_response = requests.get(image_url)
        with open('phone.png', 'wb') as file:
            file.write(img_response.content)
        print("Image saved as 'phone.png'.")
    else:
        print("No image available for product id 135.")
else:
    print("Product with id 135 not found.")

premium_products = [product for product in products if product['price'] > 800]
total_value = sum(product['price'] * product['stock'] for product in premium_products)
print(f"Total value of premium products: {total_value}")