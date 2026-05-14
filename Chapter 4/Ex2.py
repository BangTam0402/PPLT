class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Nạp tiền thành công")
        else:
            print("Nạp tiền thất bại")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Rút tiền thành công")
        else:
            print("Rút tiền thất bại")

    def get_balance(self):
        return self.__balance


name = input("Nhập tên chủ tài khoản: ")

account_1 = BankAccount(name)

deposit_amount = float(input("Nhập số tiền muốn nạp: "))
account_1.deposit(deposit_amount)

withdraw_amount = float(input("Nhập số tiền muốn rút: "))
account_1.withdraw(withdraw_amount)

print("Chủ tài khoản:", account_1.account_holder)
print("Số dư hiện tại:", account_1.get_balance())