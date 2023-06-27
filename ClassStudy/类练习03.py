class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.__salary = salary


    @property
    def salary(self):
        print('月薪为:{0},年薪为{1}'.format(self.__salary,12*self.__salary))
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if (0<salary<1000000):
            self.__salary = salary
        else :
            print('薪水录入错误，只能在0-1000000之间')


emp1 = Employee('高琪',100)
print(emp1.salary)

emp1.salary = -200






