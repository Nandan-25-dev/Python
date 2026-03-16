from expense import Expense
class Expensemanager(Expense):
    def __init__(self):
        self.expenses=[]
    def add_expense(self,name,amount,category,dates):
        expense=Expense(name,amount,category,dates)
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
                f.write(f"{e.name},{e.amount},{e.category},{e.dates}\n")
    def load_expenses(self):
        try :
            self.expenses=[]
            with open("expenses.txt","r") as f:
                for line in f :
                    name,amount,category,dates=line.strip().split(',')
                    expense=Expense(name,float(amount),category,dates)
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass
    def delete_expense(self,index):
        if 0<=index<len(self.expenses):
            removed=self.expenses.pop(index)
            print("Removed: ",removed.name)
        else:
            print("Invalid index")
    def search_expense(self,key):
        found = False
        for e in self.expenses:
            if key.lower() in e.name.lower():
                print(e.name,e.amount,e.dates,e.category)
                found=True
            if not found:
                print("No expenses found!!")
    def edit_expense(self,name,new_amount):
        for e in self.expenses:
            if e.name==name:
                e.amount=new_amount
                print("Amount Updated!")
                return
            print("No such expense or failed to update!")
    def budget_check(self,budget):
        total=0
        for e in self.expenses:
            total+=e.amount
        if total>budget:
            print("Budget exceeded!!")
        else:
            print("Remaining budget is rs",total-budget)



