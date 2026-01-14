class bank_account:
    def __init__(self,accountnumber,balance):
        self.accountnumber=accountnumber
        self.balance=balance

    def deposit(self):
        self.balance=self.balance+self.accountnumber
        return self.balance

    def withdraw(self):
        self.balance=self.balance-self.accountnumber
        return self.balance

class save_account(bank_account):
    def __init__(self,interest)
        self.interest=interest

    def calculate(self):
        self.balance=self.balance+self.interest
        return self.balance

    

