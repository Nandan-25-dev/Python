from datetime import date
from manager import Expensemanager
manager=Expensemanager()
manager.load_expenses()
while True:
    print("1. Add expense")
    print("2.View Expense")
    print("3.Total Expense")
    print("4.Save Expenses")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if (choice==1):
        category=input("Enter the category: ")
        name=input("Enter the name of the expense: ")
        amount=float(input("Enter the amount of the expense: "))
        manager.add_expense(name,amount,category,date.today())
    elif(choice==2):
        manager.view_expense()
        ch=input("Press y to delete an item and n to revert back!")
        if ch=='y':
            i=int(input("Enter index to delete!"))
        exit(0)
        manager.delete_expense(i)
    elif(choice==3):
        manager.total_expense()
    elif(choice==4):
        manager.save_expenses()
        break
    elif(choice==5):
        print("Thankyou, Exiting!")
        break
    else:
        print("Invalid choice!")
manager.save_expenses()