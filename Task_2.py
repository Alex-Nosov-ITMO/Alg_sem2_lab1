
# 2 Задание
print('2 Задание \n ')


# Функция, которая убирает лишние знаки (для 2 задания)
def clearMark(string):
    mark = [',', '.', ':', '!', '(', ')', '«', '»', '?', '<', '>', '[', ']', '/', '*', '&', '^', '%', '$', '@', '_', '=', '+', ';', '|', '- ']
    for x in mark:
        string = string.replace(x, '')

    return string


# Оригинальный текст и плагиат: убираем знаки + разбиваем по пробелу
f = open('test.txt', encoding='utf-8')
plag = f.read()
plag = clearMark(plag)
plag = plag.lower()
plag = plag.split()


f = open('оригинал.txt', encoding='utf-8')
orig = f.read()
orig = clearMark(orig)
orig = orig.lower()
orig = orig.split()


# countTriple - общее кол-во троек в плагиате (const); countPlagiat - кол-во плагиатных троек
countTriple = len(plag) - 2
countPlagiat = 0

for i in range(len(orig) - 2):
    # Шаблон - текущая тройка слов; текущий индекс слов плагиата
    shablon = [orig[i], orig[i + 1], orig[i + 2]]
    index = 0

    # Пока index <= идекс последнего слова в plag
    while index < len(plag) - 1:
        # Текущая строка из plag
        thisNumber = plag[index:index + 3]

        # Если плагиат == шаблон, то
        if thisNumber == shablon:
            # Счётчик плагиата ++; выводим совпадение; выходим из while
            countPlagiat += 1
            print(f'Совпадение {countPlagiat}: {thisNumber[0]}, {thisNumber[1]}, {thisNumber[2]}')
            break
        else:
            # Иначе:
            # index =   длина совпавшего участка     - значение префикс функции для не совпавшего элемента + 1
            index += lenMatches(thisNumber, shablon) - valuePrefix(thisNumber, shablon) + 1

print(f'\nОригинальность текста (в %): {int(100 - countPlagiat / countTriple * 100)}%')
