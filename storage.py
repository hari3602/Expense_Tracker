from Transaction import Transaction
import json

class Storage:
    def save(self, transactions):
        data = [t.__dict__ for t in transactions]
        with open("transactions.json", "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        try:
            with open("transactions.json", "r") as file:
                data = json.load(file)
                return [Transaction(t['date'], t['type'], t['category'], t['amount']) for t in data]
        except Exception as e:
            print("LOAD ERROR:", e)   
            return []