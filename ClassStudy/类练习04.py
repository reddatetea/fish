class Student:
    school = '白鹭街小学'   #类属性
    count = 0             #类属性

    def __init__(self,name,score):
        self.name = name       #实例属性
        self.score = score
        Student.count += 1

    def say_score(self):
        print('学校是:',Student.school)       #实例方法
        print(self.name,'的分数是:',self.score)

s1 = Student('高琪',80)
s1.say_score()
s2 = Student('小堂',100)
s2.say_score()

print('一共创建{0}个Student对象'.format(Student.count))