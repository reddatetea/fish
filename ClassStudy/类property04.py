class Cell:
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self,value):
        if 'alive' in value.lower():
            self.__state = 'alive'
        else :
            self.__state = 'dead'
    @property
    def is_dead(self):
        return not self.__state.lower() == 'alive'

c = Cell()
c.state = 'Alive'
print(c.state)
print(c.is_dead)