from datetime import date
import json
import os
class Expense:
    def __init__(self,name,amount,date):
        self.name=name
        self.amount=amount
        self.date=date.today()
class Expensemanager(Expense):
    def __init__(self):
        self.expenses=[]
    def add_expense(self,name,amount,date):
        expense=Expense(name,amount,date)
        self.expenses.append(expense)
    def view_expense(self):
        for e in self.expenses:
            print(e.name,":",e.amount,":",e.date)
    def total_expense(self):
        total=0
        for e in self.expenses:
            total+=e.amount
        print("Total : ",total)
    def save_expenses(self):
        with open("expenses.txt","w") as f:
            for e in self.expenses:
                f.write(f"{e.name},{e.amount},{e.date}\n")
    def load_expenses(self):
        expenses=[]
        try :
            with open("expenses.txt","r") as f:
                for line in f :
                    name,amount,date=line.strip().split(',')
                    expense=Expense(name,float(amount),date)
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass
