# Create a program to calculate sum of marks of 5 subjects and then calculate average.
# Take marks of 5 subjects as input from user.
maths = input("enter the marks of Mathematics: ")
English = input("enter the marks of English: ")
chem = input("enter the marks of Chemistry: ")
phy = input("enter the marks of Physics: ")
Hindi = input("enter the marks of Hindi: ")
Total_marks = int(maths) + int(English) + int(Hindi) + int(chem) + int(phy)
Avg = Total_marks / 5
print("Sum of the marks:", end="")
print(Total_marks)
print("Average:", end="")
print(Avg)


