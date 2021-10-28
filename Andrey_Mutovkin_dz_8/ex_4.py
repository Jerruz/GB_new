def val_checker(callback):
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            if not callback(*args, **kwargs):
                if kwargs == {}:
                    raise ValueError(f"wrong args: {', '.join([str(x) for x in args])}")
                else:
                    raise ValueError(
                        f"wrong args: {', '.join([str(x) for x in args])}, {', '.join([str(kwargs[x]) for x in kwargs.keys()])}")
            else:
                return func(*args, **kwargs)

        return wrapper

    return _wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
