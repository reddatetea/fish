class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getsize(self):
        return self.width,self.height
    def setsize(self,size):
        self.width,self.height = size

    def delsize(self):
        self.width,self.height = 0,0
    size = property(getsize,setsize,delsize,'用于描述矩形大小的属性')
print(Rectangle.size.__doc__)
help(Rectangle.size)
rect = Rectangle(4,3)
print(rect.size)
rect.size = 9,7
print(rect.width)
print(rect.height)

del rect.size
print(rect.width)
print(rect.height)