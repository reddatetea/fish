import enum
class Gender(enum.Enum):
    MALE = '男','阳刚之力'
    FEMALE = '女','柔顺之美'

    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc
    @property
    def desc(self):
        return self._desc
    @property
    def cn_name(self):
        return self._cn_name
print('FEMALE的value:',Gender.FEMALE.name)
print('FEMALE的value:',Gender.FEMALE.value)
print('FEMALE的cn_name',Gender.FEMALE.cn_name)
print('FEMALE的value:',Gender.FEMALE.desc)

