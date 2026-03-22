from expense import Expense
import csv
import json
class Expensemanager(Expense):
    def __init__(self):
        self.expenses=[]
        self.next_id=1
    def add_expense(self,dates,category,name,amount):
        expense=Expense(self.next_id,dates,category,name,amount)
        self.expenses.append(expense)
        self.next_id+=1
        self.save_expenses()
    def view_expense(self):
        for e in self.expenses:
            print(f"{[e.expense_id]} | {e.dates} | {e.category} | {e.name} | ₹{e.amount} |")
    def total_expense(self):
        total=0
        for e in self.expenses:
            total+=e.amount
        print("Total : ",total)
    def save_expenses(self):
        data=[]
        for e in self.expenses:
            data.append({
                'Eid': e.expense_id,
                'Date': e.dates,
                'Category': e.category,
                'Name': e.name,
                'Amount': e.amount})
            with open("expenses.son","w") as f:
                json.dump(data,f,indent=4)
            print("Saved to JSON!")
    def load_expenses(self):
        try :
            with open("expenses.json","r")as f:
                data=json.load(f)
                for item in data:
                    expense=Expense(item["Eid"],item["dates"],item["category"],item["name"],item["amount"])
                    self.expenses.append(expense)
            if self.expenses:
                self.next_id=max(e.expense_id for e in self.expenses)+1
        except FileNotFoundError:
            pass
    def delete_expense(self,eid):
        for e in self.expenses:
            if e.expense_id==eid:
                self.expenses.remove(e)
                print("Expense Deleted!")
                return
            print("Invalid ID")
    def search_expense(self,key):
        found = False
        for e in self.expenses:
            if key.lower() in e.name.lower():
                print(e.expense_id,e.dates,e.category,e.name,e.amount)
                found=True
            if not found:
                print("No expenses found!!")
    def edit_expense(self,eid,new_amount):
        for e in self.expenses:
            if e.next_id==eid:
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
            writer.writerow(["EID","Date(yyyy-mm-dd)","Category","Name","Amount"])
            for e in self.expenses:
                writer.writerow([e.expense_id,e.dates,e.category,e.name,e.amount])
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

