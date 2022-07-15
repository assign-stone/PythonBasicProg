# Create a program to calculate volume of cylinder for given value of radius and height.
# Take radius and height input from user.
r = input("enter radius: ")
h = input("enter height: ")
v = 1 / 3 * 3.14 * int(r) ** 2 * int(h)
print("volume of the cylinder: ", end="")
print(v)
