class Expense_track:

    def add_expense(self):
        pass
    
    def list_expense(self):
        pass

    def total_expense(self):
        pass
    
    def run(self):
        while True:
            choice = str(input("What do you wanna do (add, list, total, exit)")).strip().lower()
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
    