# Dipali_Savaliya
products={"Milk":30,"Bread":40,"Rice":60,"Apples":100,"Eggs":70}
for name,price in products.items():
    print("Name:",name)
    print("Price:",price)
    print("\n")
print("\n______________________________________")
for name,price in products.items():
    if(price <= 50):
        print("Name:",name)
        print("Price:",price)
        print("\n")
print("\n______________________________________")
a= lambda price: price * 0.20 if (price >= 80) else 0
for name,price in products.items():
    print("Name:",name,"----->","Discount:",a(price))
# print only product price is more than 80
print("\n______________________________________")
for name, price in products.items():
    if (price >= 80):
        a = lambda price: price * 0.20
        print("Name:", name)
        print("Original Price:", price)
        print("Discount:", a(price))
        print("Final Price:", price - a(price))
        print()
