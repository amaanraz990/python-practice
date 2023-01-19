# credit and debit machine
x = 50000
print("welcome")
print(f"you have amount {x}")
a  = str(input("Do you want to c or d: "))
amount = float(input("please enter amount: "))
if a == "c":
    print(f"you credited amount: {amount}")
    print(f"your current balance is ",x+amount)
elif a == "d":
    if amount <= 50000:
        print(f"your debited amount: {amount}")
        print(f"your current balance is ",x-amount)
    else:
        print(f"you have only {x} in your account")    
else:
    print("some thing went wrong")
print("thankyou")
print("exit")



           
                                                                                                                
