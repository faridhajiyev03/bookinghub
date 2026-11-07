# while True:
#     try:
#         number_1 = int(input("Enter first number: "))
#         number_2 = int(input("Enter second number: "))
#         print(f"Result: {number_1 / number_2}")
#         break
#     except ValueError:
#         print("Please enter numbers only")
#     except ZeroDivisionError as error:
#         print("Cannot divide by zero")
#
# print("Done")





try:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(f"Result: {number_1 / number_2}")
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
print("Done")



