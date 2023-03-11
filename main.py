'''def delcp(x):
    arr = ",<>.[]?!/*&^%$@()_-=+:;|"
    for i in arr:
        x = x.replace(i, ' ')
    while "  " in x:
        x = x.replace("  ", " ")
    return x


f = open('text.txt')
text = f.read()
text = delcp(text)
text = text.lower()
text = text.split()

f = open('wiki.txt')
wiki = f.read()
wiki = delcp(wiki)
wiki = wiki.lower()
wiki = wiki.split()

count = 0
p = 0
while p < len(text) - 3:
    flag = False
    k = 0
    while k < len(wiki) - 3:
        pattern = ''.join(text[p:p + 3])
        if pattern == ''.join(wiki[k:k + 3]):
            print(pattern, ''.join(wiki[k:k + 3]))
            count += len(pattern)
            flag = True
            k += 3
            break
        else:
            k += 1
    if flag == True:
        p += 3
    else:
        p += 1

print(f'Процентное сожержание плагиата в тексте составляет {int(count / len("".join(text)) * 100)} %.')


# Создание строки
def createString():
    # Строка из простых чисел - глобальная переменная
    global numbersString

    # Функция, которая возвращает: простое число или нет
    def prost(n):
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

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
    return numbersString


m = createString()

for z in range(10, 100):
    patern = str(z)
    # Формирование смещений


    S = set()   # Уникальные символы в шаблоне
    lenPattern = len(patern)  # Длина шаблон
    dic = {}  # Словарь смещений

    for i in range(lenPattern - 2, -1, -1):
        if patern[i] not in S:
            dic[patern[i]] = lenPattern - i -1
            S.add(patern[i])


    if patern[lenPattern - 1] not in S:
        dic[patern[lenPattern - 1]] = lenPattern

    dic['*'] = lenPattern




    print(dic)


    example = m
    lenExample = len(example)

    print(example)

    i = lenPattern - 1

    while (i < lenExample):
        k = 0
        for j in range(lenPattern - 1, -1, -1):
            if example[i - k] != patern[j]:
                if j == lenPattern - 1:
                    offset = dic[example[i]] if dic.get(example[i], False) else dic['*']

                else:
                    offset = dic[patern[j]]

                i += offset
                break
            k+=1
        if j == 0:

            print(f'шаблон найден по индексу {i - k + 1}')
            i += 1

'''




def palindrom(str):
    max_count = -1
    max_str = ''
    for i in range(len(str)-1):
        for j in range(i+1, len(str)):
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


stroka = 'АААВАГБАБББВБГГБАГБАБГВАВБГБАБАГБАББВАВБВВВГГБГВ'

print(palindrom(stroka))