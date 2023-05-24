class Bird:
    def fly(self):
        print('我在天空里自由自在地飞翔')
class Ostrich(Bird):
    def fly(self):
        print('我只能在地上奔跑')
os = Ostrich()
os.fly()
