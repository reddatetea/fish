class MyRectangle :
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def GetArea(self):
        rectange_area = self.width*self.height
        print('矩形的面积是{}'.format(rectange_area))

    def GetPerimeter(self):
        rectange_Perimeter = 2*(self.width+self.height)
        print('矩形的周长是{}'.format(rectange_Perimeter))

rectangle = MyRectangle(100,100,300,300)
rectangle.GetArea()
rectangle.GetPerimeter()














