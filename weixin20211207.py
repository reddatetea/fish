'''
微信字段：Nickname昵称，remarkName，备注，Sex，性别，Signature个性签名，'Province': '云南', 'City': '昆明'
'''
import itchat
import logging

logging.basicConfig(filename="", level=logging.INFO)


# 一个带参数的装饰器,类装饰器，语法糖效果等同于foo = timeit(foo)
def log_print(new_var):
    def middle(func):
        def wrapper(*args, **kwargs):
            logging.info("start print {} ...".format(new_var))
            try:
                return func(*args, **kwargs)
            except Exception as e:
                pass
            logging.info("{} print end...".format(new_var))

        return wrapper

    return middle


class PythonWechat(object):
    def __init__(self):
        self.___nickname = list()
        self.__sex = list()
        self.all_friends = list()

    def login_wechat(self):
        itchat.auto_login(hotReload=True)
        logging.info("login successfully")

    def get_friend(self):
        '''获取全部好友'''
        self.all_friends = itchat.get_friends(update=True)[1:]
        logging.info("already get all friends")
        return self.all_friends

    def get_attribute(self, var):
        total_list = list()
        for i, j in enumerate(self.all_friends):
            # logging.info(j)
            one_attribute = j[var]
            # logging.info(j[var])
            total_list.append(one_attribute)
        return total_list

    @log_print("nickname")
    def get_nickname(self):
        '''获取昵称'''
        self.___nickname = self.get_attribute("NickName")

    @log_print("sex")
    def get_sex(self):
        '''获取性别'''
        self.__sex = self.get_attribute("Sex")
        man, woman, not_man_woman = 0, 0, 0
        for sex_split in self.__sex:
            if sex_split == 0:
                woman += 1
            elif sex_split == 1:
                man += 1
            elif sex_split == 2:
                not_man_woman += 1
        logging.info("have already get all man's sex")
        return man, woman, not_man_woman

    def main(self):
        # self.login_wechat()
        # self.get_friend()
        # man_num, woman_num, not_man_woman_num = self.get_sex()
        # logging.info(
        #     "man have {},woman have {},people that not konw have {}.".format(man_num, woman_num, not_man_woman_num))
        itchat.send('Hello, filehelper', toUserName='filehelper')

if __name__ == '__main__':
    pw = PythonWechat()
    pw.main()