# Now, the Assignment:
# Create a User class that has an association with the BankAccount class . You should not have to change anything in the BankAccount class .
# For example, from the User class we should be able to deposit money into the user's account:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    # other methods

    def make_deposit(self, amount):
    	# your code here




# But our User class does not have a self.account_balance attribute. What it does have is an instance of a BankAccount by the name of self.account. That means that we'll be mirroring the methods created in the BankAccount class like make_deposit (and other methods referencing self.account_balance). But we'll be calling on the BankAccount class to do most of the work! That's the goal of this assignment, and you may find that you do not have to add much logic if any.
# Remember in our User methods, we can now access the BankAccount class through our self.account attribute, like so:

class User:
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
    	print(self.account.balance)		# or access its attributes
