def type_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(f'{func.__name__}(', end='')
        if kwargs != {}:
            print(', '.join(
                [
                    ', '.join([str(type(x)) for x in args]),
                    ', '.join([str(type(kwargs[x])) for x in kwargs.keys()])
                ]
            ), end='')
        else:
            print(', '.join([str(type(x)) for x in args]), end='')

        print(f') -> {type(result)}')

        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def test(*args, **kwargs):
    return args, kwargs


print(test(1, 2, 4, k=1))
