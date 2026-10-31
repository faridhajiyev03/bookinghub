service_name = "Стрижка"     # str, текст в кавычках
price = 25                   # int, целое число
duration_hours = 1.5         # float, дробное число
is_available = True          # bool, только True или False

print(f"Услуга: {service_name}, цена: {price} AZN, Duration: {duration_hours} hours")
print(type(price))           # <class 'int'>
print(type(service_name))
print(type(duration_hours))
print(type(is_available))

