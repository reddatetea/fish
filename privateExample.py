class BankAccount:
    def __init__(self, accountHolder):
        # BankAccount方法可以访问self._balance，
        # 但该类之外的代码不能访问
        self._balance = 0 ❶
        self._name = accountHolder ❷
        with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')

    def deposit(self, amount):
         if amount <= 0: ❸
            return # 不允许存款为负数
         self._balance += amount
         with open(self._name + 'Ledger.txt', 'a') as ledgerFile: ❹
             ledgerFile.write('Deposit ' + str(amount) + '\n')
             ledgerFile.write('Balance is ' + str(self._balance) + '\n')

    def withdraw(self, amount):
        if self._balance < amount or amount < 0: ❺
            return # 余额不足，或者取款金额是负数
        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile: ❻
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')

acct = BankAccount('Alice') # 为Alice创建一个账户
acct.deposit(120) # _balance可以通过deposit()进行修改
acct.withdraw(40) # _balance可以通过withdraw()进行修改

# 虽然不建议在BankAccount外修改_name和_balance，但能够修改：
acct._balance = 1000000000 ❼
acct.withdraw(1000)

acct._name = 'Bob' # 现在我们要修改Bob的账目！ ❽
acct.withdraw(1000) # 这笔取款被记录到BobLedger.txt中了！