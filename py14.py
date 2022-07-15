# Create a program to speed of a vehicle for given distance and time.
# Take time and distance input from user.
D = input("Enter the value of distance(in meters) = ")
T = input("Enter the value of Time(in sec) = ")
S = float(D) / float(T)
print("Speed of the vehicle: ", end="")
print(S, end="")
print(" m/s")
