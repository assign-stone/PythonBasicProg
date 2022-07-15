# Create a program to calculate total price for given quantity and rate of a product
# then also calculate discount of 23%
# and print Total Price, discounted amount and net amount after reducing discount.
# (Take rate of product Rs.78.23 and take quantity input from user)

q = input("Enter Quantity of the product: ")
R = 78.23
Total_price = int(q) * float(R)
discount = float(Total_price) * 0.23
net = float(Total_price) - float(discount)
print("Total price:", end="")
print(Total_price)
print("Discounted price:", end="")
print(discount)
print("Net amount:", end="")
print(net)
