from datetime import date
from manager import Expensemanager
manager=Expensemanager()
manager.load_expenses()
while True:
    print("1. Add expense")
    print("2.View Expense")
    print("3.Total Expense")
    print("4.Save Expenses")
    print("5.Search Expense")
    print("6.Edit Expense")
    print("7.Check Budget")
    print("8.Export to CSV")
    print("9.Statistics")
    print("10.Exit")
    choice=int(input("Enter your choice: "))
    if (choice==1):
        dates=input("Enter the date (YYYY-mm-dd):  ")
        category=input("Enter the category: ")
        name=input("Enter the name of the expense: ")
        amount=float(input("Enter the amount of the expense: "))
        manager.add_expense(name,amount,category,dates)
    elif(choice==2):
        manager.view_expense()
        ch=input("Press y to delete an item or enter any key to revert back: ")
        if ch=='y':
            i=int(input("Enter id to delete: "))
            manager.delete_expense(i)
        print("Redirected Back!")
    elif(choice==3):
        manager.total_expense()
    elif(choice==4):
        manager.save_expenses()
        break
    elif choice==5:
        keyword=input("Enter expense name: ")
        manager.search_expense(keyword)
    elif choice==6:
        key=input("Enter the expense ID: ")
        n_amount=float(input("Enter the new amount for the expense: "))
        manager.edit_expense(id,n_amount)
    elif choice==7:
        budget=float(input("Enter the budget amount: "))
        manager.budget_check(budget)
    elif choice==8:
        manager.export_csv()
    elif choice==9:
        manager.statistics()
    elif(choice==10):
        print("Thankyou, Exiting!")
        break
    else:
        print("Invalid choice!")
manager.save_expenses()