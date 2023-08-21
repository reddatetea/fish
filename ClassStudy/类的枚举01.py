import enum

Season = enum.Enum('Season',('SPRING','SUMMER','FALL','WINTER'))
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(Season['SUMMER'])
print(Season(3))

for name,member in Season.__members__.items():
    print(name,'>=','member',',',member.value)


