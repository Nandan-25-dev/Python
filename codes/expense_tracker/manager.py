from expense import Expense
import csv
class Expensemanager(Expense):
    def __init__(self):
        self.expenses=[]
        self.next_id=1
    def add_expense(self,name,amount,category,dates):
        expense=Expense(self.next_id,name,amount,category,dates)
        self.expenses.append(expense)
        self.id+=1
    def view_expense(self):
        for e in self.expenses:
            print(e.next_id,":",e.category,":",e.name,":",e.amount,":",e.dates)
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
                    expense=Expense(id,name,float(amount),category,dates)
                    self.expenses.append(expense)
        except FileNotFoundError:
            pass
    def delete_expense(self,id):
        for e in self.expenses:
            if e.id==id:
                self.expenses.remove(e)
                print("Expense Deleted!")
                return
            else:
                print("Invalid ID")
    def search_expense(self,key):
        found = False
        for e in self.expenses:
            if key.lower() in e.name.lower():
                print(e.name,e.amount,e.dates,e.category)
                found=True
            if not found:
                print("No expenses found!!")
    def edit_expense(self,id,new_amount):
        for e in self.expenses:
            if e.id==id:
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
    def export_csv(self):
        with open("expenses.csv","w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["EID","Date(yyyy-mm-dd)","Name","Category","Amount"])
            for e in self.expenses:
                writer.writerow([e.id,e.dates,e.name,e.category,e.amount])
        print('Expenses exported to CSV!')
    def statistics(self):
        if not self.expenses:
            print("No Expenses")
            return
        total=sum(e.amount for e in self.expenses)
        avg=total/len(self.expenses)
        max_exp=max(self.expenses,key=lambda e:e.amount)
        min_exp=min(self.expenses,key=lambda e:e.amount)
        print("Total = rs",total,"\n")
        print("Average= rs",avg,"\n")
        print("Maximum expenses= rs",max_exp.amount,"\n")
        print("Minimum expenses= rs",min_exp.amount,"\n")

