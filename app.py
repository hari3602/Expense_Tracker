from datetime import datetime
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
        try:
            datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")
            return
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

    def print_transactions(self, data):
        """Helper method to print transaction data."""
        print("Index \t Date \t Transction type \t Category \t Amount \n")
        print("-" * 60)
        for txn in data:
            if isinstance(txn, tuple):  # For filtered transactions (income/expense)
                index, transaction = txn
            else:  # For all transactions
                index, transaction = data.index(txn) + 1, txn
            sign = "+" if transaction.type == "income" else "-"
            print(f"{index}\t{transaction.date}\t{transaction.type}\t{transaction.category}\t{sign}{transaction.amount}")

    def list_cli(self):
        list_filter = input("List of (Income/Expense/all):").strip().lower()
        if list_filter == "all":
            data = self.service.list_transactions()
            self.print_transactions(data)
        elif list_filter in ["income", "expense"]:
            data = self.service.list_transaction_by_type(list_filter)
            self.print_transactions(data)
        else:
            print("Enter valid input")

    def total_cli(self):
        total = self.service.total_transactions()
        print(f"Income: {total['income']} \n Expense: {total['expense']} \n Balance: {total['balance']}")

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
    