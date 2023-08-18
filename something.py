from abc import *

class Transferable(ABC):
    @staticmethod
    def transfer(self, destination_account, amount):
        pass

class TransferService:
    def __init__(self, source_account, destination_account):
        self.source_account = source_account
        self.destination_account = destination_account

    def transfer(self, amount):
        self.source_account.transfer(self.destination_account, amount)

class Account(Transferable):
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Недостаточный баланс")

    def get_balance(self):
        return self.balance

    def transfer(self, destination_account, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            destination_account.deposit(amount)
        else:
            raise ValueError("Недостаточный баланс")

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)

    def get_interest_rate(self):
        return self.interest_rate

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, fee_percentage=0):
        super().__init__(account_number, balance)
        self.fee_percentage = fee_percentage

    def deduct_fees(self):
        fees = self.balance * (self.fee_percentage / 100)
        self.balance -= fees

    def get_fee_percentage(self):
        return self.fee_percentage

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer_funds(self, source_account_number, destination_account_number, amount):
        source_account = self.find_account(source_account_number)
        destination_account = self.find_account(destination_account_number)

        if source_account and destination_account:
            transfer_service = TransferService(source_account, destination_account)
            transfer_service.transfer(amount)
        else:
            raise ValueError("Исходный или целевой аккаунт не найден")

save = SavingsAccount(account_number = '007', balance = 1000, interest_rate = 10)
bank = Bank()
bank.add_account(save)
print(save.get_balance())
print(bank.find_account('007'))