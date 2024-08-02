from threading import Thread, Lock
import threading

lock1 = Lock()
lock2 = Lock()

class BankAccount():

    def __init__(self, balance=0):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        with lock1:
            for _ in range(5):
                self.balance += amount
                print(f'Депозит {amount}, новый баланс счета {self.balance}')

    def withdraw(self, amount):
        with lock2:
            for _ in range(5):
                if amount < self.balance:
                    self.balance -= amount
                    print(f'Снятие {amount}, новый баланс счета {self.balance}')
                else:
                    raise ValueError('На счете недостаточно средств')

account1 = BankAccount(1000)

deposit_thread = threading.Thread(target=BankAccount.deposit, args=(account1, 100))
withdraw_thread = threading.Thread(target=BankAccount.withdraw, args=(account1, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()