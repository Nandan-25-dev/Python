from datetime import date
class Expense:
    def __init__(self,name,amount,category):
        self.name=name
        self.amount=amount
        self.dates=date.today()
        self.category=category