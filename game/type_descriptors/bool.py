class Bool:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, bool):
            raise TypeError('Must be bool')
        instance.__dict__[self.name] = value


    def __set_name__(self, owner, name):
        self.name = name