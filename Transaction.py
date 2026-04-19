class Transaction:
    def __init__(self, date, t_type, category, amount):
        self.date = date
        self.type = t_type
        self.category = category
        self.amount = amount
        # return {"date": self.date, "type": self.type, "category": self.category, "amount": self.amount}