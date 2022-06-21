#Скрипт конвертации чисел двоичной и десятичной системы счисления
#Без обработки ошибок
#Автор ArtemKAF

def bin2dec(number):
    c_number = number
    print(c_number, type(c_number))

def dec2bin(number):
    c_number = number
    print(c_number, type(c_number))

if __name__ == '__main__':
    number = int(input("Введите число для конвертации:"))
    num_sys1 = int(input("Введите основание системы счисления этого числа:"))
    num_sys2 = int(input("Введите основание желаемой системы счисления:"))

    if num_sys2 == 10:
        bin2dec(number)
    elif num_sys2 == 2:
        dec2bin(number)
    else:
        print(f"Программа не умеет переводить числа в систему счисления с основанием {num_sys2}")
    print("Конец программы")
