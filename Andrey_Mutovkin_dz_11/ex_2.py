class ZeroDivision(ZeroDivisionError):
    pass


user_data = 0
while user_data != "":
    user_data = input(">> ")
    try:
        try:
            print(eval(user_data))
        except ZeroDivisionError:
            raise ZeroDivision(f"Была попытка деления на ноль: \"{user_data}\"")
    except ZeroDivision as zd:
        print(zd)
