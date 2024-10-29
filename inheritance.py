# library management system
# Parent/Base/Superclass
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def displayinfo(self):
        return f'Book Title: {self.title} Author: {self.author}'
# child/derived/sub class
class LibraryBook(Book):
    def __init__(self, title, author, isbn, copies_available):
        super().__init__(title, author)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f'{self.title} borrowed. Copies left {self.copies_available}'
        else:
            return f'No. of copies {self.title} available'
    def return_book(self):
        self.copies_available+=1
        return f'{self.title} returned. Copies left {self.copies_available}'

book1 = LibraryBook("Gifted Hands", "Ben Carson", 676734, 15)
print(book1.displayinfo())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.return_book())


class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else: return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."
    def get_balance(self):
        return f"Account balance: ${self.balance}"
# Derived class for Savings Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}"
# Derived class for Checking Account
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.balance}"
        else:
            return "Withdrawal amount exceeds balance and overdraft limit."
# Example usage
savings = SavingsAccount("123456", "Alice", 1000)
checking = CheckingAccount("789012", "Bob", 500)
# Deposit and withdraw from SavingsAccount
print(savings.deposit(200))
# Deposited $200. New balance: $1200
print(savings.apply_interest()) # Interest of $24.00 applied. New balance: $1224.00
print(savings.withdraw(300)) # Withdrew $300. Remaining balance: $924.00 # Deposit and withdraw from CheckingAccount
print(checking.deposit(100)) # Deposited $100. New balance: $600
print(checking.withdraw(650)) # Withdrew $650. Remaining balance: -$50
print(checking.get_balance()) # Account balance: -$50