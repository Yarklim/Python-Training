# ===================== Инкапсуляция =====================


class BankAccount:
    def __init__(self, balance):
        self.__balance = (
            balance  # Инкапсуляция баланса (напрямую нельзя обращаться к переменной)
        )

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


bank = BankAccount(1000)

bank.deposit(100_000)
print(bank.get_balance())  # 101000
print(bank.__balance)  # ошибка
