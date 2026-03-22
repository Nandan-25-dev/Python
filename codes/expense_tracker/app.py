from flask import Flask
from manager import Expensemanager
manager=Expensemanager()
manager.load_expenses()
app = Flask(__name__)
@app.route("/")
def home():
    print("Debug Expenses: ",manager.expenses)
    output= ""
    for e in manager.expenses:
        output+=f"{e.expense_id}-{e.dates}-{e.category}-{e.name}-{e.amount}<br>"
    return str(output)
if __name__=="__main__":
    app.run(debug=True)