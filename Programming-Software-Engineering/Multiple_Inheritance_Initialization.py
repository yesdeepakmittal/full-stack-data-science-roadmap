# https://stackoverflow.com/a/50465583
class Base1:
    def __init__(self):
        print('Base1.__init__')

class Base2:
    def __init__(self):
        print('Base2.__init__')

class Derived(Base1, Base2):
    def __init__(self):
        super().__init__()
        super(Base1,self).__init__()

d = Derived()