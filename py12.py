# Create a program to calculate simple interest for given values of P, R and T.
# Take P, R, and T input from user.
print("Enter the values below:")
p = input("Principal : ")
r = input("Rate : ")
t = input("Time : ")
si = int(p) * float(r) * float(t) / 100
print("Simple Interest is:", end="")
print(si)
