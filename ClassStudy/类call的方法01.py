class SalaryAccount:

    def __call__(self,salary):
        yearSalary = salary*12
        daySalary = salary/30
        hourSalary = daySalary/8

        #return

dict(montySalary = salary,yearSalary = yearSalary,daySalary = daySalary,hourSalary = hourSalary)

s = SalaryAccount()
print(s(5000))
