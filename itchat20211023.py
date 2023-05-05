import itchat

itchat.auto_login(hotReload=True)
friends=itchat.get_friends('1142760803')
print(friends)