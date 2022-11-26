import sys
def input_natural(message):  # Метод обработки ввода натурального числа
    while True:
        try:
            number = int(input(f'Введите натуральное число (от 1 до {sys.maxsize}) {message}: '))
            # sys.maxsize - максимально возможное значение переменной типа integer в данной версии Python
            if number < 1:
                print('Ошибка ввода. Попробуйте еще раз\n')
                continue
            return number
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз\n')
denominations = [64, 32, 16, 8, 4, 2, 1]    # Список номиналов купюр
rest = input_natural('- сумму выплаты')
print('Потребуется:')
count = 0   # Счетчик кол-ва купюр
for denomination in denominations:
    if rest // denomination != 0:
        count += rest // denomination   # Обновление счетчика (соответствует целочисленной частности остатка и номинала)
        print(f'{rest // denomination} куп. номинала {denomination}')
    rest = rest % denomination  # Теперь сумма выплат - остаток от очередного деления суммы на номинал

print(f'Всего: {count} куп.')
input('Работа программы завершена. Для выхода из консоли нажмите Enter')
