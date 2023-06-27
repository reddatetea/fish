class Canvas :
    def draw_pic(self,shape):
        print('----开始绘图----')
        shape.draw(self)

class Rectangle :
    def draw(self,canvas):
        print('在{}上绘制矩形'.format(canvas))

class Triangle :
    def draw(self,canvas):
        print('在{}上绘制三角形'.format(canvas))

class Circle :
    def draw(self,canvas):
        print('在{}上绘制圆形'.format(canvas))

c = Canvas()
c.draw_pic(Rectangle())
c.draw_pic(Triangle())
c.draw_pic(Circle())