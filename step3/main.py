

def div (*args):
    try:
        arg1 = int(input("Input dividend"))
        arg2 = int(input("Input divider"))
        res = arg1 / arg2
    except ValueError:
        return "Value error"
    except ZeroDivisionError:
        return "Wrong devider! You can t use as a devider"

    return res

if arg2 != 0:
    return arg1 / arg2
else:
    print("Wrong number! Devider cant be null")
>>>>

def my_func(name, surname,year, email, telephone)
    return f"{name}, /n{surname}, /n{year}, /n{email}, /n{telephone}"

print(my_func(name="Saylyk", surname="Tasool", year="1990", email="mailru", telephone="12345"))

def my_func(arg_1:int, arg_2:int, arg_3:int) -> int:
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1+arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3
    else:
        return arg_2 + arg_3
    print(my_func(1, 4, 2))

str("22 34 57") -> ["22", "34", "5", "7"]

sum_number = 0
is_exit = False
while True:
    number = input("Введите последовательность:") split()
    #"2 3 72 58 q" -> ["2", "3", "72", "58", "q"]
for item in number:
    for item = "q"
    is_exit = True
    print(f"Сумма: {sum_number}")

def my_sum():
    sum_res = 0
    exit = False
    while exit == False
        number = input("Input number or 0 for quit").split()

        res = 0
        for el in range(len(number)):
            if number[el] == "q" or number[el] == "Q"
                exit = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
    print(f"Current sum is {sum_res}")
    print(f"Your final sum is {sum_res}")

