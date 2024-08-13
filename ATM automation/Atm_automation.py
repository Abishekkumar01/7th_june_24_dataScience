# project 1
# ATM automation 

Name = input("Pls enter your name:")
print("hello,",Name)
message = """
Type 1 >>> Check Balance 
Type 2 >>> Deposit
Type 3 >>> Withdrawal
"""
print(message)

task = int(input("Pls enter any of the options:"))
available_amount = 5000
if task >=1 and task <=3:
    print("Welcome to the virtual bank...")
    if task == 1:
        print("Your available amount is:",available_amount)
        print("Thank You for banking us!")

    elif task == 2:
        
        deposit_amount = int(input("Pls enter your deposit amount:"))
        if deposit_amount > 500:
            available_amount += deposit_amount
            print("You have successfully deposited your deposit amount",deposit_amount)
            print("Your available amount is:",available_amount)
            print("Thank your for banking us!")
            
        else:
            print("Pls enter more than 500 Rs")
        


    elif task == 3:
        withdraw_amount = int(input("Pls enter your withdraw amount:"))
        if withdraw_amount <= available_amount:
            available_amount -= withdraw_amount
            print("You have successfully withdrawn your amount",withdraw_amount)
            print("Your available amount is:",available_amount)
            print("Thank you for banking us!")
        else: 
            print("Insufficient fund",available_amount)         

else:
    print("Pls select within 1-3")
