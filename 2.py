import time
print("put your card into the atm")
time.sleep(5)
password=1234
balance=5000
pin=int(input("enter your pin number"))
if password==pin:
    while(True):
        choice=input("1.balance enquiry\n2.withdrawl\n3.deposit\n4.change the pin\n5.exit")
        if choice=="1":
            print("your available balance is:",balance)
        elif choice=="2":
            print("enter the amount to withdraw")
            withdraw=int(input())
            balance=balance-withdraw
            print("Amount withhdrawed")
            print("Available Balance is :",balance)
        elif choice=="3":
            print("enter the money to deposit")
            deposit=int(input())
            balance=balance+deposit
            print("Money Deposited")
            print("Available balance:",balance)
        elif choice=="4":
            pin1=int(input("enter the new pin"))
            pin2=int(input("confirm your pin"))
            if pin1==pin2:
                pin=pin1
                print("pin changed  successfully")
                print("your new pin is",pin)
            else:
                print("enter the correct pin")

        else:
            print("enter the valid option for right transaction")
        print("do you want to perform other transaction (y/n)")
        i=input()
        if i=='y':
            pass
        else:
            break
else:
    print("wrong pin entered")
print("THANK YOU")
print("VISIT AGAIN")
