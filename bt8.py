# List products 
products = ["cat", "banana", "obama", "car", "cow", "alibaba", "batman"]

# Get product name input
product_name = input("Enter product name: ")

# List store the result indexes contains the product name
product_indexes = []

# Iterate through the product list
for product in products: 
    # Check if the product string contains the product name (substring)
    if product_name in product:
        product_indexes.append(products.index(product))

print("Vị trí các index chứa tên '{}': ".format(product_name), product_indexes)