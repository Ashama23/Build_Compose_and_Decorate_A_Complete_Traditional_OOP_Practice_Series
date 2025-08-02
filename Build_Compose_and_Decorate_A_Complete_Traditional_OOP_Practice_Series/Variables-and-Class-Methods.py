class Bank:
    bank_name = "MyBank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_details(self):
        print(f"Bank: {self.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:,.2f}")

account1 = Bank("Alice", 1500.75)
account2 = Bank("Bob", 2340.50)

print("--- Initial Bank Details ---")
account1.display_details()
print("-" * 20)
account2.display_details()
print("\n")

Bank.change_bank_name("Global Finance")

print("--- Updated Bank Details ---")
account1.display_details()
print("-" * 20)
account2.display_details()