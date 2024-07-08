# Task 1
x = input("Enter a four-digit ticket number: ")
y = list(x)
if int(y[0]) + int(y[1]) == int(y[2]) + int(y[3]):
    print("you're right.")
else:
    print("Error")
# Task 2
number = input("Enter six number: ")
if number == number[::-1]:
    print("You`re right")
else:
    print("Enter new numbers")
# Task 3
r = 4
x = float(input("X coordinates: "))
y = float(input("Y coordinates: "))
if x**2 + y**2 <= r**2:
    print(f"point lies in the middle of the circle ({x}, {y})")
else:
    print(f"point liesn`t in the middle of the circle({x}, {y})")
