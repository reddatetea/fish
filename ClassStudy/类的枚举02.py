import enum
class Orientation (enum.Enum):
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'
    def info(self):
        print('这是一个代表方向[%s]的枚举'%self.value)
print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
print(Orientation['WEST'])
print(Orientation('南'))
Orientation.EAST.info()

for name,member in Orientation.__members__.items():
    print('name','>=',',',member.value)