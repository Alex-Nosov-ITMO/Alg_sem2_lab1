
import random


# Создаем случайную фигуру
def randomFigure():
    letter = ['А', 'Б', 'В', 'Г', ]
    points = []

    while len((points)) != 4:
        points += [{'x': random.randint(1, 100), 'y': random.randint(1, 100)}]

    result = {letter[i]: {'firstPoint': points[i], 'secondPoint': points[(i + 1) % 4]} for i in range(4)}

    return result


# {'А': {'firstPoint': {'x': 59, 'y': 64}, 'secondPoint': {'x': 20, 'y': 8}},
# 'Б': {'firstPoint': {'x': 20, 'y': 8}, 'secondPoint': {'x': 72, 'y': 47}},
# 'В': {'firstPoint': {'x': 72, 'y': 47}, 'secondPoint': {'x': 59, 'y': 96}},
# 'Г': {'firstPoint': {'x': 59, 'y': 96}, 'secondPoint': {'x': 59, 'y': 64}}}


# Возвращает, пересекаются ли две прямые или нет
def comparisonSides(rebroFirst, rebroSecond):
    x1_1, y1_1 = rebroFirst['firstPoint']['x'], rebroFirst['firstPoint']['y']
    x1_2, y1_2 = rebroFirst['secondPoint']['x'], rebroFirst['secondPoint']['y']
    x2_1, y2_1 = rebroSecond['firstPoint']['x'], rebroSecond['firstPoint']['y']
    x2_2, y2_2 = rebroSecond['secondPoint']['x'], rebroSecond['secondPoint']['y']

    # составляем формулы двух прямых
    A1 = y1_1 - y1_2
    B1 = x1_2 - x1_1
    C1 = x1_1 * y1_2 - x1_2 * y1_1
    A2 = y2_1 - y2_2
    B2 = x2_2 - x2_1
    C2 = x2_1 * y2_2 - x2_2 * y2_1

    # решаем систему двух уравнений
    if A1 == 0 or B1 * A2 - B2 * A1 == 0: return False

    if B1 * A2 - B2 * A1 != 0:
        y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        x = (-C1 - B1 * y) / A1
        # проверяем, находится ли решение системы (точка пересечения) на первом отрезке, min/max - потому
        # что координаты точки могут быть заданы не по порядку возрастания
        dX1Min, dX1Max = min(x1_1, x1_2), max(x1_1, x1_2)
        dY1Min, dY1Max = min(y1_1, y1_2), max(y1_1, y1_2)
        dX2Min, dX2Max = min(x2_1, x2_2), max(x2_1, x2_2)
        dY2Min, dXY2Max = min(y2_1, y2_2), max(y2_1, y2_2)
        return dX1Min <= x <= dX1Max and dY1Min <= y <= dY1Max and dX2Min <= x <= dX2Max and dY2Min <= y <= dXY2Max


# Проходимся по всем комбинациям рёбер для двух фигур
def bruteforceSide(firstFigure, secondFigure):
    str = ''

    for elementFirst in firstFigure:
        for elementSecond in secondFigure:
            if comparisonSides(firstFigure.get(elementFirst, 0), secondFigure.get(elementSecond, 0)):
                str += elementFirst + elementSecond

    return str


userNumber = int(input('Введите число случайных четырехугольников: '))
arrayFigure = [randomFigure() for _ in range(userNumber)]
resultString = ''

for i in range(userNumber - 1):
    for j in range(i + 1, userNumber):
        resultString += bruteforceSide(arrayFigure[i], arrayFigure[j])

print('Строка пересечений: ', resultString, '\n')


def palindrom(str):
    max_count = -1
    max_str = ''
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            k = 0
            p = -1
            count = 0
            flag = True
            while k - p < len(str[i:j]):
                if str[i:j][k] == str[i:j][p]:
                    count += 1
                    k += 1
                    p -= 1
                else:
                    flag = False
                    break
            if flag == True and count > max_count:
                max_count = count
                max_str = str[i:j]

    return max_str


print('Самая длинная подстрока, являющаяся полиндромом: ', palindrom(resultString), '\n')
pal = palindrom(resultString)


# Алгоритм Кнута-Морриса-Пратта


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
shablon = pal

# Текущий индекс строки
index = 0

# Пока index <= индекс последнего элемента numbersString - 1
while index <= len(resultString) - 2:

    # Текущая подстрока
    thisNumber = resultString[index:index + len(shablon)]

    # Если строка в шаблоне, то
    if thisNumber == shablon:
        # В словаре значение соотв. числа ++
        print('Индекс полиндрома: ', index, '\n')
        break
    else:
        # Иначе:
        # index =   длина совпавшего участка     - значение префикс функции для не совпавшего элемента + 1
        index += lenMatches(thisNumber, shablon) - valuePrefix(thisNumber, shablon) + 1


def search(str):
    countMax = 0
    for i in range(len(str) - 1):
        letter = {'А': 0, 'Б': 0, 'В': 0, 'Г': 0}
        thisString = ''
        for j in range(i, len(str)):
            letter[str[j]] += 1
            thisString += str[j]

            if int(letter['А'] % 2 == 1) + int(letter['Б'] % 2 == 1) + int(letter['В'] % 2 == 1) + int(
                    letter['Г'] % 2 == 1) <= 1:
                if len(thisString) > countMax:
                    countMax = len(thisString)
                    ans = thisString
    return ans


print('Самая длинная подстрока, из которой можно сделать полиндом: ', search(resultString), '\n')


# Hash для двузначного числа
def getHash(string):
    b = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3}
    return sum([b[string[i]] * 4 ** (len(string) - i - 1) for i in range(len(string))])


shablon = search(resultString)
shablonHash = getHash(search(resultString))

for i in range(len(resultString) - 1):

    thisNumber = resultString[i:i + len(shablon)]

    thisHash = getHash(thisNumber)

    if thisHash == shablonHash:
        print('Индекс самой длинной подстроки, из которой можно сделать полиндом: ', i, '\n')
        print(
            f'Количество букв: А = {shablon.count("А")}, Б = {shablon.count("Б")}, В = {shablon.count("В")}, Г = {shablon.count("Г")}')
        break




