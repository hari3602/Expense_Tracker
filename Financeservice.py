from Transaction import Transaction
from storage import Storage
from datetime import datetime

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
    
    def list_transaction_by_type(self,t_type):
        return [(i+1, self.transactions[i]) for i in range(len(self.transactions)) if self.transactions[i].type==t_type]

    
    def total_transactions(self):
        total_income = sum(transaction.amount for transaction in self.transactions if transaction.type == 'income')
        total_expense = sum(transaction.amount for transaction in self.transactions if transaction.type == 'expense')
        return {'income': total_income,'expense': total_expense,'balance':total_income - total_expense}
    
    def category_summary(self):
        # category = list({txn.category for txn in self.transactions})
        category_total = {}
        for txn in self.transactions:
            if txn.category in category_total:
                if txn.type == "income":
                    category_total[txn.category]["income"] += txn.amount
                elif txn.type == "expense":
                    category_total[txn.category]["expense"] += txn.amount
            else:
                category_total[txn.category] = {"income": 0, "expense": 0}
                if txn.type == "income":
                    category_total[txn.category]["income"] = txn.amount
                elif txn.type == "expense":
                    category_total[txn.category]["expense"] = txn.amount
        return category_total
    
    def monthly_summary(self):
        monthly_summary ={}
        for transaction in self.transactions:
            date_obj = datetime.strptime(transaction.date, "%d/%m/%Y")
            month_key = date_obj.strftime("%m/%Y")
            if month_key not in monthly_summary:
                monthly_summary[month_key] = {"income": 0, "expense": 0, "balance":0}
            if transaction.type == "income":
                monthly_summary[month_key]["income"] += transaction.amount
            elif transaction.type == "expense":
                monthly_summary[month_key]["expense"] += transaction.amount
            monthly_summary[month_key]["balance"] = monthly_summary[month_key]["income"]-monthly_summary[month_key]["expense"]
        return monthly_summary
