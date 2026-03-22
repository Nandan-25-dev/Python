from datetime import date
from manager import Expensemanager
manager=Expensemanager()
manager.load_expenses()
while True:
    print("\n--------EXPENSE TRACKER--------")
    print("\n========CLI ver.1.0============")
    print("\t|1. Add expense  |")
    print("\t|2.View Expense  |")
    print("\t|3.Total Expense |")
    print("\t|4.Search Expense|")
    print("\t|5.Edit Expense  |")
    print("\t|6.Check Budget  |")
    print("\t|7.Export to CSV |")
    print("\t|8.Statistics    |")
    print("\t|9.Exit          |")
    choice=int(input("Enter your choice: "))
    if (choice==1):
        dates=input("Enter the date (YYYY-mm-dd):  ")
        category=input("Enter the category: ")
        name=input("Enter the name of the expense: ")
        try:
            amount=float(input("Enter the amount of the expense: "))
        except ValueError:
            print('Invalid Amount')
            continue
        manager.add_expense(dates,category,name,amount)
    elif(choice==2):
        manager.view_expense()
        ch=input("Press y to delete an item or enter any key to revert back: ")
        if ch=='y':
            i=int(input("Enter id to delete: "))
            manager.delete_expense(i)
        print("Redirected Back!")
    elif(choice==3):
        manager.total_expense()
    elif choice==4:
        keyword=input("Enter expense name: ")
        manager.search_expense(keyword)
    elif choice==5:
        key=input("Enter the expense ID: ")
        n_amount=float(input("Enter the new amount for the expense: "))
        manager.edit_expense(id,n_amount)
    elif choice==6:
        budget=float(input("Enter the budget amount: "))
        manager.budget_check(budget)
    elif choice==7:
        manager.export_csv()
    elif choice==8:
        manager.statistics()
    elif(choice==9):
        print("Thankyou, Exiting!")
        break
    else:
        print("Invalid choice!")
manager.save_expenses()