#Interactive text based Coffee Shop simulator 

#  Define the prices
coffee_price = 5
muffin_price = 4

# Ask the customer for the number of coffee and muffins
num_coffees = int(input("Enter the number of coffees: "))
num_muffins = int(input("Enter the number of muffins: "))

# Calculate the subtotal
subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price)

# Calculate the tax (6%)
tax = subtotal * 0.06

# Calculate total
total = subtotal + tax

# Print the receipt
print("*********************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print("1")
print("Number of muffins bought")
print("2")
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
