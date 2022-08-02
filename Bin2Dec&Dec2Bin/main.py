#Скрипт конвертации чисел двоичной и десятичной системы счисления
#Автор ArtemKAF


def bin2dec(number):
    i = 0
    conv = 0
    while number // 10 != 0:
        if number % 10:
            conv = conv + 2 ** i
            number = number // 10
            i += 1
        else:
            number = number // 10
            i += 1
    conv += 2 ** i
    return conv


def dec2bin(number):
    i = 0
    conv = ""
    while number != 0:
        i += 1
        if number % 2:
            conv = conv.rjust(i, '1')
        else:
            conv = conv.rjust(i, '0')
        number = number // 2
    return conv


if __name__ == '__main__':
    number = int(input("Введите число для конвертации:"))
    num_sys = int(input("Введите основание желаемой системы счисления:"))

    if num_sys == 10:
        print(bin2dec(number))
    elif num_sys == 2:
        print(dec2bin(number))
    else:
        print(f"Программа не умеет переводить числа в систему счисления с основанием {num_sys}")

