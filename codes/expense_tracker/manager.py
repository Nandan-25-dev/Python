from expense import Expense
from datetime import date
class Expensemanager(Expense):
    def __init__(self):
        self.expenses=[]
    def add_expense(self,category,name,amount,dates):
        expense=Expense(category,name,amount,dates)
        self.expenses.append(expense)
    def view_expense(self):
        for e in self.expenses:
            print(e.category,":",e.name,":",e.amount,":",e.dates)
    def total_expense(self):
        total=0
        for e in self.expenses:
            total+=e.amount
        print("Total : ",total)
    def save_expenses(self):
        with open("expenses.txt","w") as f:
            for e in self.expenses:
                f.write(f"{e.category},{e.name},{e.amount},{e.dates}\n")
    def load_expenses(self):
        expenses=[]
        try :
            with open("expenses.txt","r") as f:
                for line in f :
                    category,name,amount,dates=line.strip().split(',')
                    expense=Expense(category,name,float(amount),self.dates)
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass
    def delete_expense(self,index):
        if 0<=index<len(self.expenses):
            removed=self.expenses.pop(index)
            print("Removed: ",removed.name)
        else:
            print("Invalid index")

