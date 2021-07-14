

class BoardSize:
    """
        BoardSize must be Tuple[int, int] with positive values
    """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, tuple):
            raise TypeError(f'{self.name} must be Tuple[int, int] with positive values')
        if len(value) > 2 or len(value) == 0:
            raise ValueError(f'BoardSize cannot be with size {len(value)} it must contain 1 or 2 elemets')
        for index_, element in enumerate(value):
            if not isinstance(element, int):
                raise ValueError(f'Element {index_}({element}) must be int')
            if element < 1:
                raise ValueError(f'Element {index_}({element}) must be positive')
        instance.__dict__[self.name] = value


    def __set_name__(self, owner, name):
        self.name = name