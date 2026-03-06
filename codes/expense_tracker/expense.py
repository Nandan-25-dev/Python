from datetime import date
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
