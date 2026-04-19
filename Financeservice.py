from Transaction import Transaction
from storage import Storage

class FinanceService:
    def __init__(self):
        self.storage = Storage()
        self.transactions = []

    def add_transaction(self, date, t_type, category, amount):
        transaction = Transaction(date, t_type, category, amount)
        self.transactions.append(transaction)
        self.storage.save(self.transactions)

    def delete_transaction(self,txn_index):
        try:
            self.transactions.pop(txn_index-1)
            self.storage.save(self.transactions)
        except IndexError:
            print("Invalid delete index")
            return

    def list_transactions(self):
        return(self.transactions)
    
    def total_transactions(self):
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.type == 'income')
        total_expense = sum(transaction.amount for transaction in self.transactions if transaction.type == 'expense')
        return {'income': total_income,'expense': total_expense,'balance':total_income - total_expense}