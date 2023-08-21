class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码，工资是:', self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print('我是一个顾客，我的爱好是: %s,地址是%s' % (self.favorite, self.address))


# Manager继承了Employee、Customer
class Manager(Customer,Employee):
    # 重写父类的构造方法
    def __init__(self,favorite, address,salary):
        print('--Manager的构造方法--')
        # 通过super()函数调用父类的构造方法
        #super().__init__(favorite, address)  # 调用第一个父类！
        # 与上一行代码的效果相同
        super(Manager, self).__init__(favorite, address)

        # 使用未绑定方法调用父类的构造方法
        # Employee.__init__(self,salary)
        Employee.__init__(self,salary)


# 创建Manager对象
m = Manager('IT产品', '广州',25000)
m.work()  # ①
m.info()  # ②