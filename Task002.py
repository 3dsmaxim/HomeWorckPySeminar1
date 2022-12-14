# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Вариант рас #################################################

# numberEnter = str(input('Введите 3-х значное число: '))
# while int(numberEnter) < 100 or int(numberEnter) > 999:
#     numberEnter = str(
#         input('Неверный ввод \nПовторите вводе 3-х значного числа: '))
# print('Сумма цифр трехзначного числа = ', int(numberEnter[0]) + int(numberEnter[1]) + int(numberEnter[2]))


# Вариант два #################################################


def enter(num):
    while int(num) < 100 or int(num) > 999:
        num = str(input('Неверный ввод \nПовторите вводе 3-х значного числа: '))
    return num

def sum(num):
    count = 0
    numSum = 0
    while count < len(num):
        numSum += int(num[count])
        count += 1
    return numSum


numberEnter = enter(str(input('Введите 3-х значное число: ')))

print('Сумма цифр трехзначного числа = ', sum(numberEnter))
