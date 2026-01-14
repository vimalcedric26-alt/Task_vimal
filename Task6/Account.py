class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.account_number = account_number
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount ")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount ")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance, interest_rate):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        return interest

    def add_interest(self):
        interest = self.calculate_interest()
        self.deposit(interest)
        return interest


class CurrentAccount(BankAccount):
    def __init__(self, account_number, initial_balance, minimum_balance):
        super().__init__(account_number, initial_balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        remaining_balance = self.get_balance() - amount
        if remaining_balance < self.minimum_balance:
            raise ValueError("Cannot withdraw: minimum balance ")
            return super().withdraw(amount)

savings = SavingsAccount("SA123", 1000, 5)
print("Savings Balance:", savings.get_balance())
print("Interest Earned:", savings.add_interest())
print("Updated Balance:", savings.get_balance())

current = CurrentAccount("CA456", 2000, 500)
print("Current Balance:", current.get_balance())
current.withdraw(1000)
print("Balance after withdrawal:", current.get_balance())
