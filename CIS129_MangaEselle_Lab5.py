#declare loop 
keep_going = "y"

# set the loop 
while keep_going == "y": 
    #declare the variables 
    total_bottles = 0  
    today_bottles = 0 
    total_payout = 0 # will be store total_bottles times . 10 
    counter = 1 
    NBR_OF_DAYS = 7

    #Add days 
    while counter <= NBR_OF_DAYS:
         today_bottles = input('Enter number of bottles returned for day ' + str(counter) + ':')
         total_bottles += int(today_bottles)
         counter += 1 
 

    #calculate payout 
    PAYOUT_PER_BOTTLE = .10 
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

    #collect total payout 
    print("The total number of bottles collected is " + str(total_bottles))
    print("The total payout is $", format(total_payout, '.2f'))

    #the next week 
    print('Do you want to enter another week\'s worth of data?')

    #decide if there is another week 
    keep_going = input('(Enter y or n): ')


