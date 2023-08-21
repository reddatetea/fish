import wizcoin

change = wizcoin.WizCoin(9, 7, 20)
print(change.sickles) # 打印7
change.sickles += 10
print(change.sickles) # 打印17

pile = wizcoin.WizCoin(2, 3, 31)
print(pile.sickles) # 打印3
pile.someNewAttribute = 'a new attr' # 创建一个新的特性
print(pile.someNewAttribute)