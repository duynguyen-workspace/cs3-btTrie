products = ["cat", "banana", "obama", "car", "cow", "alibaba", "batman"]

product_name = input("Enter product name: ")

product_indexes = []

for product in products: 
    if product.__contains__(product_name):
        product_indexes.append(products.index(product))

print("Vị trí các index chứa tên '{}': ".format(product_name), product_indexes)