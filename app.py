class Expense_track:
    
    def __init__(self):
        self.expense = {}

    def add_expense(self):
        category = str(input("For what thing do you spend for:")).strip()
        amount = int(input("how much you spend: "))
        if category not in self.expense:
            self.expense[category] = amount
        else:
            self.expense[category] += amount

    
    def list_expense(self):
        print(self.expense)

    def total_expense(self):
        money = self.expense.values()
        money = list(money)
        total = sum(money)
        print(total)
    
    def run(self):
        while True:
            choice = str(input("What do you wanna do (add, list, total, exit)\n\t")).strip().lower()
            if choice == "add":
                self.add_expense()
            elif choice == "list":
                self.list_expense()
            elif choice == "total":
                self.total_expense()
            elif choice == "exit":
                break
            else:
                print("invalid choice")

if __name__ == "__main__":
    app = Expense_track()
    app.run()
    