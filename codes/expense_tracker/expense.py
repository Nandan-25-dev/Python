from datetime import date
class Expense:
    def __init__(self,name,amount,dates):
        self.name=name
        self.amount=amount
        self.dates=date.today()