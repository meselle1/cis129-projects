#declare the local variables 
monthlySaLes = 0 #monthly sales amount 
storeAmount = 0 # store bonus amount 
empAmount = 0 # employee bonus amount 
salesIncrease = 0 # percent of sales increase 
prompt1 = "What were last month's sales?: "
prompt2 = "What was last month's sale increase?: "

# monthly sales 
monthlySales = float(input(prompt1))

# store bonus amount  
if monthlySales >= 110000:
    storeAmount= 6000 
elif monthlySaLes >= 100000:
       storeAmount = 5000
elif monthlySaLes >= 90000:
    storeAmount = 4000
elif storeAmount >= 80000:
    storeAmount = 3000 
else: 
       storeAmount = 0

# percent increase in the sales
salesIncrease = float(input(prompt2))
salesIncrease = salesIncrease / 100

# emp amount 
if salesIncrease >= .05:
     empAmount = 75 
elif salesIncrease >= .04:
     empAmount = 50 
elif salesIncrease >= .03:
     empAmount = 40 
else:
     empAmount = 0 

# prints bonus information 
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
     print('Congrats! You have reached the highest bonus amounts possible! ')
