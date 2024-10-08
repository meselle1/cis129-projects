#Interactive text based Coffee Shop simulator 

#  Define the prices
coffee_price = 5
muffin_price = 4
bagel_price = 3
donut_price = 6

# Ask the customer for the number of coffee and muffins
num_coffees = int(input("Enter the number of coffees: "))
num_muffins = int(input("Enter the number of muffins: "))
num_bagels = int(input("Enter the number of bagels: "))
num_donuts = int(input("Enter the number of donuts: "))

# Calculate the subtotal
subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price) + (num_bagels * bagel_price) + (num_donuts * donut_price)

# Calculate the tax (6%)
tax = subtotal * 0.06

# Calculate total
total = subtotal + tax

# Print the receipt
print("*********************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print("1")
print("Number of muffins bought?")
print("2")
print("Number of bagels bought?")
print("2")
print("Number of donuts bought?")
print("4")
print("*********************************")
print("")
print("*********************************")
print("My Coffee and Muffin Shop Receipt")
print(f"Number of coffees: {num_coffees} x ${coffee_price:.2f} = ${num_coffees * coffee_price:.2f}")
print(f"Number of muffins: {num_muffins} x ${muffin_price:.2f} = ${num_muffins * muffin_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (6%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("*********************************")
print("")
print("Thank you!")

