import uuid
from datetime import date

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.budgets = []

    def add_budget(self, budget):
        self.budgets.append(budget)

    def remove_budget(self, budget_name):
        self.budgets = [budget for budget in self.budgets if budget.name != budget_name]



class Budget:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category_name):
        self.categories = [category for category in self.categories if category.name != category_name]

    def get_total_spent(self):
        return sum(category.get_total_spent() for category in self.categories)

class Category:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def remove_transaction(self, transaction_id):
        self.transactions = [transaction for transaction in self.transactions if transaction.id != transaction_id]

    def get_total_spent(self):
        return sum(transaction.amount for transaction in self.transactions)


class Transaction:
    def __init__(self, amount, description, category):
        self.id = uuid.uuid4()
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date.today()

    def __repr__(self):
        return f"Transaction({self.amount}, {self.description}, {self.category}, {self.date})"



# Create a user
user = User("john_doe", "password123")

# Create a budget
monthly_budget = Budget("Monthly Budget", 2000)

# Add the budget to the user
user.add_budget(monthly_budget)

# Create categories
groceries = Category("Groceries")
rent = Category("Rent")

# Add categories to the budget
monthly_budget.add_category(groceries)
monthly_budget.add_category(rent)

# Add transactions to categories
groceries.add_transaction(Transaction(100, "Weekly groceries", "Groceries"))
rent.add_transaction(Transaction(900, "Monthly rent", "Rent"))

# Check total spending
print(f"Total spent in groceries: ${groceries.get_total_spent()}")
print(f"Total spent in rent: ${rent.get_total_spent()}")
print(f"Total spent in budget: ${monthly_budget.get_total_spent()}")





        