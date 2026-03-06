from expense import Expense
from expense import Expensemanager
from datetime import date
manager=Expensemanager()
while True:
    print("1. Add expense\n")
    print("2.View Expense\n")
    print("3.Total Expense\n")
    print("4.Exit")
    choice=int(input("Enter your choice: "))
    if (choice==1):
        name=input("Enter the name of the expense: ")
        amount=float (input("Enter the amount of the expense: "))
        manager.add_expense(name,amount,date)
    elif(choice==2):
        manager.view_expense()
    elif(choice==3):
        manager.total_expense()
    elif(choice==4):
        print('Exiting thank you!')
        break
    else:
        print("Invalid choice!")
