invested = float(input("Please enter an initial principal: "))

rate = float(input("Enter the annual interest rate: "))

year = 0
amount = invested

while amount <= invested * 3 :      
  #while loop for Simple interest

    amount = amount + amount * (rate)/100
    year = year + 1


print("Amount of time is: %d years"%(year))