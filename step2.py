service_price = float(input("Enter service price: "))
duration_hours = float(input("Enter duration hours: "))

total_price = service_price * duration_hours
print(f'Total: {total_price:.2f} AZN')