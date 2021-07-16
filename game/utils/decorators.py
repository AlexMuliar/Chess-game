import functools

def execute_until_valid(func):
    functools.wraps(func)
    def wrap(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as ex:
                print(*ex.args)
    return wrap