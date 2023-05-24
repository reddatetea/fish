class Inventory:
    item = '鼠标'
    quantity = 2000
    def change(self,item,quantity):
        self.item = item
        self.quantity = quantity

iv = Inventory()
iv.change('显示器',500)
print(iv.item)
print(iv.quantity)
print(Inventory.item)
print(Inventory.quantity)

Inventory.item = '类变量item'
Inventory.quantity = '类变量quantity'
print(iv.item)
print(iv.quantity)

iv.item = '实例变量item'
iv.quantity = '实例变量quantity'
print(Inventory.item)
print(Inventory.quantity)

