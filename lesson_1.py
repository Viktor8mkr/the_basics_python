# tack_1
print("Как вас зовут? ")
name = input()
print("Сколько вам лет? ")
years = str(input())
print("Здравствуйте, " + name + "! " + "Ваш возраст " + years)

# tack_2
time_sec = int(input('Введите время в секундах: '))
hours = time_sec // 3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time_sec % 3600) // 60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time_sec % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print(
        'Количество полученных часов превышает количество часов в сутка, скоректируйте ввод.')
else:
    print(f'Московское время: {hours_res}:{minutes_res}:{seconds_res}')

# tack_3
n = input('Введите число: ')
nn = int(n + n)
nnn = int(n + n + n)
n = int(n)
result = n + nn + nnn
print(result)

# tack_4
n = int(input("Введите целое положительное число "))
max1 = n % 10
print(max1)
while n >= 1:
    n = n // 10
    print(n)
    if n % 10 > max1:
        print(n)
        print(max1)
        max1 = n % 10
        print(max1)
    elif n > 9:
        pass
print("Максимальное цифра в числе ", max1)

# tack_5
plus = int(input('Введите значение прибыли: '))
minus = int(input('Введите значение издержек: '))
people = int(input('Ввдите количество работников: '))

if plus > minus:
    print('Выручка больше издержек')
    clear_plus = plus - minus
    rent = clear_plus / plus
    print('Рентабельность {} выручки {}: {:.2f}'.format('нашей', 'составила',
                                                        rent))
    clear_for_person = float(clear_plus / people)
    print(
        'Прибыль фирмы в расчете на одного сотрудника: %s' % clear_for_person)
else:
    print('Фирма работает в убыток')

# tack_6

a = int(input("Введите расстояние первой пробежки в км: "))
b = int(input("Введите целевой результат в км: "))

counter = 1  # начальное значение счетчика дней

while a < b:
    a *= 1.1  # расчет расстояния пробежки
    counter += 1  # увеличение счетчика дней

# вывод результата
print(f"На {counter}-й день спортсмен достиг результата — не менее {b} км")
