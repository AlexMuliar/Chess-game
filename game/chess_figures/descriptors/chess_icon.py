
class ChessIconCode:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not value in range(0x2654, 0x2660):
            raise ValueError('No chess icon code')
        instance.__dict__[self.name] = chr(value)


    def __set_name__(self, owner, name):
        self.name = name