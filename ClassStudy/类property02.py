class User:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def getfullname(self):
        return self.first + ',' + self.last
    def setfullname(self,fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]
    fullname = property(getfullname,setfullname)
u = User('悟空','孙')
print(u.fullname)
u.fullname = '八戒,朱'
print(u.first)
print(u.last)