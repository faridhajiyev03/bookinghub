prices = {"haircut": 25, "massage": 40, "manicure": 18}

# 1. Show all services (loop over the dictionary, print every pair)
for name, price in prices.items():
    print(f"{name}: {price} AZN")

# 2. Ask the user ONE time (no loop here!)
service = input("Enter the name of service: ")

# 3. Check if this key exists in the dictionary
if service in prices:
    print(f"Price: {prices[service]} AZN")
else:
    print("Service not found")





