from Transaction import Transaction
from Financeservice import FinanceService
from storage import Storage

class FinanceTracker:
    
    def __init__(self):
        self.service = FinanceService()
        self.storage = Storage()
        self.service.transactions = self.storage.load()

    def add_cli(self):
        date = input("Enter date: ")
        t_type = input("Type (income/expense): ").strip().lower()
        if t_type not in ["income", "expense"]:
            print("Invalid type")
            return
        category = input("Category: ")
        try:
            amount = int(input("Amount: "))
        except ValueError:
            print("Invalid amount")
            return
        
        self.service.add_transaction(date, t_type, category, amount)

    def delete_cli(self):
        try:
            txn_index = int(input("Index of transaction: "))
        except ValueError:
            print("Invalid index")
            return
        self.service.delete_transaction(txn_index)

    def list_cli(self):
        data = self.service.list_transactions()
        print("Index \t Date \t Transction type \t Category \t Amount \n")
        print("-"*60)
        for index, txn in enumerate(data, start=1):
            sign = "+" if txn.type == "income" else "-"
            print(f"{index}\t{txn.date}\t{txn.type}\t{txn.category}\t{sign}{txn.amount}")

    def total_cli(self):
        summary = input("summary of (all/category): ").strip().lower()
        if summary == "all":
            total = self.service.total_transactions()
            print(f"Income: {total['income']} \n Expense: {total['expense']} \n Balance: {total['balance']}")
        elif summary == "category":
            total = self.service.category_summary()
            for category in total:
                print(f"{category}: Income: {total[category]['income']}, Expense: {total[category]['expense']}, Balance: {total[category]['income'] - total[category]['expense']}")

    def run_cli(self):
        while True:
            choice = str(input("What do you wanna do (add, delete, list, total, exit)\n\t")).strip().lower()
            if choice == "add":
                self.add_cli()
            elif choice == "delete":
                self.delete_cli()
            elif choice == "list":
                self.list_cli()
            elif choice == "total":
                self.total_cli()
            elif choice == "exit":
                break
            else:
                print("invalid choice")

if __name__ == "__main__":
    app = FinanceTracker()
    app.run_cli()
    