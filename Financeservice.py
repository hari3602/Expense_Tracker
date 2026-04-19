from Transaction import Transaction

class FinanceService:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, t_type, category, amount):
        transaction = Transaction(date, t_type, category, amount)
        self.transactions.append(transaction)

    def list_transactions(self):
        return(self.transactions)
    
    def total_transactions(self):
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.type == 'income')
        total_expense = sum(transaction.amount for transaction in self.transactions if transaction.type == 'expense')
        return {'income': total_income,'expense': total_expense,'balance':total_income - total_expense}