#Скрипт конвертации чисел двоичной и десятичной системы счисления
#Без обработки ошибок
#Автор ArtemKAF

def num_sys_conv(number, num_sys1, num_sys2):
    c_number = number
    print(c_number)


if __name__ == '__main__':
    print("Введите число для конвертации:")
    number = input()
    print("Введите основание системы счисления этого числа:")
    num_sys1 = input()
    print("Введите основание желаемой системы счисления:")
    num_sys2 = input()
    num_sys_conv(number, num_sys1, num_sys2)
    print("Конец программы")
