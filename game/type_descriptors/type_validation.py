class TypeValidatior:
    def __init__(self, type_) -> None:
        self._type = type_


    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError(f'Must be {self._type}')
        instance.__dict__[self.name] = value


    def __set_name__(self, owner, name):
        self.name = name