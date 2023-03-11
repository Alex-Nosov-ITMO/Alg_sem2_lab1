import time

# Создание строки
def createString():
    # Строка из простых чисел - глобальная переменная
    global numbersString

    # Функция, которая возвращает: простое число или нет
    def prost(n):
        return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

    # Список простых чисел; 1ое простое число
    numbers, prostNumber = [], 2

    # Пока в списке нет 500 чисел
    while len(numbers) != 500:
        # Если очередное число простое, то добавляем в список
        if prost(prostNumber):
            numbers += [str(prostNumber)]

        # Счётчик ++
        prostNumber += 1

    # Склеиваем все числа в одну строчку
    numbersString = ''.join(numbers)


# Создание словаря
def createDateNumber():
    # Словарь, в котором ключ - двузначное число,
    # Значение - кол-во совпадений соотв. числа
    global dateNumber

    # Словарь вида: {10: 0, 11: 0, 12: 0, 13: 0 .... 99: 0}
    dateNumber = {i: 0 for i in range(10, 100)}


# Вывод результата
def result():
    # отсортированный по ключам словарь - глобальная переменная
    global sortNumber
    sortNumber = dict(sorted(dateNumber.items(), key=lambda x: x[1], reverse=True)[:5])

    print('  Самые популярные двузначные числа:')
    for x in sortNumber:
        print(f'  Число = {x}, количество повторов = {sortNumber.get(x, 0)}')


# Вывод метода алгоритма
def methodString(name):
    print(f'Алгоритм: {name}')


# 2 пустые строки
def finish():
    print('\n')


# Наивный алгоритм
start1 = time.time()

methodString('наивный')

createString()

createDateNumber()

# Проходимся по всем двойкам, идущих подряд
for i in range(len(numbersString) - 1):
    # thisNumber - двузначное число (может быть, с знач. нулем)
    thisNumber = int(numbersString[i:i + 2])

    # Если у числа нет незнач. нуля, то
    # Кол-во этого числа ++
    if thisNumber >= 10:
        dateNumber[thisNumber] += 1

result()

finish()

end1 = time.time()


# Алгоритм Рабина-Карпа

start2 = time.time()

methodString('Рабина-Карпа')


createString()


createDateNumber()


# Hash для двузначного числа
def getHashTwoDigit(string):
    return int(string[0]) * 10 + int(string[1])


allHashShablon = [getHashTwoDigit(str(i)) for i in range(10, 100)]

for i in range(len(numbersString) - 1):
    thisNumber = numbersString[i:i + 2]
    thisHash = getHashTwoDigit(thisNumber)

    if thisHash in allHashShablon:
        dateNumber[int(thisNumber)] += 1

result()
finish()
end2 = time.time()

# Алгоритм Бойера-Мура

start3 = time.time()

methodString('Бойера-Мура')


createString()

createDateNumber()


i = 0
while not (i == len(numbersString) - 2):
    # thisNumber - двузначное число (может быть, с знач. нулем)
    thisNumber = int(numbersString[i:i + 2])

    # Проверям всевозможные условия совпадений
    if (thisNumber >= 10) and (thisNumber <= 99):
        dateNumber[int(thisNumber)] += 1
        i += 1
    elif thisNumber >= 1:
        i += 1
    else:
        i += 2


result()

finish()

end3 = time.time()


# Алгоритм Кнута-Морриса-Пратта

start4 = time.time()

methodString('Кнута-Морриса-Пратта')

createString()

createDateNumber()


# Префикс-функция для какой-то строки
# 'abcdabcd' --> [0, 0, 0, 1, 2, 3, 4]
def getPiForThisString(string):
    # Для 1го элемена Префикс-функция = 0
    piArray = [0]

    # Проходимся по ост. символам
    for i in range(1, len(string)):
        # Отрезаем всё, что правее текущего символа
        # 'abcdabcd' (i = 3) --> 'abcd'
        thisString = string[:i + 1]

        # Проходимся по всем случаям |суффикс| = |префикс|
        # если суффикс == префикс, то добавляем индекс текущего символа
        # Иначе 0 (если ни разу не будет хорошего случая)
        array = [i if thisString[:i] == thisString[len(thisString) - i:] else 0 for i in range(1, len(thisString))]

        # Добавляем макс число из array в список
        piArray += [max(array)]
    return piArray


# Функция, которая высчитывает совпадение строк (слева-направо)
# ('abcc', 'abad') -> 2
def lenMatches(string, shablon):
    # Счётчик совпадений
    count = 0

    # Проходимся по символам
    for i in range(len(string)):
        # Если совпадают, то count ++
        if string[i] == shablon[i]:
            count += 1
        # Иначе выводим count и завершаем ф-ию
        else:
            return count

    # Если не было случая 'else', то выводим count
    return count


# Функция, которая высчитывает значение префикс функции для не совпавшего эл-та
def valuePrefix(thisString, shablon):
    # Индекс несовп. элемента
    index = lenMatches(thisString, shablon)

    # Возвращаем из Префикс-функции для шаблона элемент с индексом index
    return getPiForThisString(shablon)[index]


# Подходящие числа
shablon = [str(i) for i in range(10, 100)]

# Текущий индекс строки
index = 0

# Пока index <= индекс последнего элемента numbersString - 1
while index <= len(numbersString) - 2:

    # Текущая подстрока
    thisNumber = numbersString[index:index + 2]

    # Если строка в шаблоне, то
    if thisNumber in shablon:
        # В словаре значение соотв. числа ++
        dateNumber[int(thisNumber)] += 1
        # index ++
        index += 1
    else:
        # Иначе:
        # index =   длина совпавшего участка     - значение префикс функции для не совпавшего элемента + 1
        index += lenMatches(thisNumber, shablon) - valuePrefix(thisNumber, shablon) + 1

result()

finish()

end4 = time.time()



print("Время работы наивного алгоритма: ", end1 - start1)
print("Время работы алгоритма Рабина-Карпа: ", end2 - start2)
print("Время работы алгоритма Бойера-Мура: ", end3 - start3)
print("Время работы алгоритма Кнута-Морриса-Пратта: ", end4 - start4)
