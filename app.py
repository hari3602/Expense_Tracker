import json

class Finance_tracker:
    
    def __init__(self):
        with open("transactions.json", "r") as file:
            self.transactions = json.load(file)

    def add_transaction(self):
        date = str(input("Enter the date of the transaction (YYYY-MM-DD): ")).strip()
        type = str(input("Enter the type of transaction (income/expense): ")).strip().lower()
        category = str(input("Enter the category of the transaction: ")).strip()
        amount = float(input("Enter the amount of the transaction: "))
        self.transactions.append({"date": date, "type": type, "category": category, "amount": amount})
        with open("transactions.jsonwha", "w") as file:
            json.dump(self.transactions, file, indent=4)
    
    def list_transactions(self):
        for txn in self.transactions:
            print(f"Date: {txn['date']}, Type: {txn['type']}, Category: {txn['category']}, Amount: {'+' if txn['type'] == 'income' else '-'}{txn['amount']}")

    def total_transactions(self):
        total_income = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'income')
        total_expense = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'expense')
        print(f"Total Income: {total_income}")
        print(f"Total Expense: {total_expense}")

    def run(self):
        while True:
            choice = str(input("What do you wanna do (add, list, total, exit)\n\t")).strip().lower()
            if choice == "add":
                self.add_transaction()
            elif choice == "list":
                self.list_transactions()
            elif choice == "total":
                self.total_transactions()
            elif choice == "exit":
                break
            else:
                print("invalid choice")

if __name__ == "__main__":
    app = Finance_tracker()
    app.run()
    