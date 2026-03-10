from datetime import date
class Expense:
    def __init__(self,name,amount,date1,category):
        self.name=name
        self.amount=amount
        self.dates=date.today()
        self.category=category