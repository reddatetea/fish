class SalaryAccount:
    def __init__(self,salary):
        self.salary = salary


    def __call__(self):
        # monthSalary = salary
        # yearSalary = salary*12
        # daySalary = salary/30
        # hourSalary = daySalary/8

        #return
dict(montySalary=self.salary, yearSalary=12 * self.salary, daySalary=self.salary / 30,hoursalrry=self.salary / 30 / 8)




s = SalaryAccount(5000)
print(s.a)