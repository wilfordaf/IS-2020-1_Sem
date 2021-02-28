import codecs  # импортируем необходимые библиотеки для чтения utf-8 и качественного удаления из строки символов
import re


def editorlen(str1, str2):  # функция, считающая длину редактирования
    numofexecutions = 0
    letters = [0] * 33
    cntof1 = 0
    l = min(len(str1), len(str2))
    ind = True
    if len(str1) - 2 > len(str2):  # если длины строк отличаются > 2 символа, то ошибка неисправима
        return len(str1) - len(str2)
    for i in range(l):  # смотрим прямой порядок букв и его соответствие
        if str1[i] != str2[i]:
            numofexecutions += 1
            ind = False
    for i in range(len(str1)):  # записываем буквы 1 и 2 слов в массив сортировкой подсчётом
        if 1103 >= ord(str1[i]) >= 1072:
            letters[ord(str1[i]) - 1072] += 1
    for i in range(len(str2)):
        if 1103 >= ord(str2[i]) >= 1072:
            letters[ord(str2[i]) - 1072] += 1

    if ind:  # если в прямом порядке букв не найдено различий, возвращаем разницу длин строк <2, ошибка исправима
        return max(len(str1) - len(str2), len(str2) - len(str1))
    for i in range(33):  # считаем кол-во букв, которые не нашли пару
        if letters[i] == 1:
            cntof1 += 1
    if cntof1 + max(len(str1) - len(str2), len(str2) - len(str1)) <= 2 and str1[0] == str2[0] and str1[-1] == str2[-1]:
        # если сумма кол-ва "неспаренных" букв и разности длин меньше 2, то ошибка исправима, т.к. пропуски в начале и
        # конце мы исправим последним return, то тут смотрим на совпадение 1 и последней буквы, т.к. по этому условию
        # пропуск в середине слова
        return cntof1 + max(len(str1) - len(str2), len(str2) - len(str1))
    elif cntof1 + max(len(str1) - len(str2), len(str2) - len(str1)) <= 2 and str1[0] != str2[0] and str1[-1] == str2[
        -1]:
        return cntof1 + max(len(str1) - len(str2), len(str2) - len(str1)) + 2
        # если же нашли анаграмму вместо слова с пропуском, то +2, чтобы программа рассмотрела в приоритете 1 случай
    return numofexecutions + max(len(str1) - len(str2), len(str2) - len(str1))  # возвращаем слова, где нет
    # пропущенных букв, но нужны замены и/или пропуск в начале или конце


fin = codecs.open("task1.txt", "r", "utf_8_sig")  # открываем файлы задания и словаря, записываем данные в массивы
dictionary = open("dict1.txt", "r")
fout = open("answer.txt", "w")
fout1 = open("newtext.txt", "w")
array = fin.read().split()
dic = []
frequencies = []
for line in dictionary:
    dic.append(line.split()[0])
    frequencies.append(line.split()[1])
text = array.copy()

bool = False  # задание 1
cnt = 0
for i in range(len(array)):  # удаляем ненужные символы из строк, переводим в строчную раскладку
    array[i] = re.sub(r"[:!?,;.:«()»]", '', array[i])
    array[i] = array[i].lower()
    if array[i] == "—":
        cnt += 1
for i in range(len(array) - cnt):
    if array[i] == '—':
        array.pop(i)

numberofwords = 0  # задание 2
numberofdifferentwords = 0
numberofdifferentwordsindic = 0
arrayofdif = []
arrayofmistakes = []
for i in range(len(array)):  # считаем количество слов, различных словоформ, различных словоформ, которые
    # присутствуют в словаре, записывая их в массив для дальнейшей работы, ошибки, т.е. если словоформа не нашлась
    # в словаре
    numberofwords += 1
    numberofdifferentwords += 1
    arrayofdif.append(array[i])
    if array.index(array[i]) != i:
        numberofdifferentwords -= 1
        arrayofdif.pop()
for i in range(len(arrayofdif)):
    if arrayofdif[i] in dic:
        numberofdifferentwordsindic += 1
    else:
        arrayofmistakes.append(arrayofdif[i])
print(numberofwords, numberofdifferentwords, numberofdifferentwordsindic, "old", file=fout)

print(' '.join(arrayofmistakes), file=fout)
numofmistakes = numberofdifferentwords - numberofdifferentwordsindic  # задание 3
changers = []
changer = ""
for word1 in arrayofmistakes:  # сравниваем слова из списка ошибок со словарём, ищем наименьшее количество
    # исправлений для каждого конкретного слова, записываем наиболее уместный вариант в changers. Если нашли замену,
    # исправляем ошибку в тесте
    minimum = 10 ** 9
    for word2 in dic:
        if editorlen(word1, word2) < minimum:
            minimum = editorlen(word1, word2)
            changer = word2
    if minimum <= 2:
        changers.append(changer)
    else:
        changers.append("не найдено")
for j in range(len(text)):
    for i in range(len(arrayofmistakes)):
        if text[j] == arrayofmistakes[i] and changers[i] != "не найдено":
            text[j] = changers[i]
numberofwordsnew = 0  # задание 4
# заного считаем количество слов, различных словоформ, различных словоформ, которые
# присутствуют в словаре, ошибки, т.е. если словоформа не нашлась в словаре
numberofdifferentwordsnew = 0
numberofdifferentwordsindicnew = 0
arrayofdifnew = []
arrayofmistakesnew = []
for i in range(len(array)):
    numberofwordsnew += 1
    numberofdifferentwordsnew += 1
    arrayofdifnew.append(array[i])
    if array.index(array[i]) != i:
        numberofdifferentwordsnew -= 1
        arrayofdifnew.pop()
for i in range(len(arrayofdifnew)):
    if arrayofdifnew[i] in dic:
        numberofdifferentwordsindicnew += 1
    else:
        arrayofmistakesnew.append(arrayofdifnew[i])
print(numberofwordsnew, numberofdifferentwordsnew, numberofdifferentwordsindicnew, "new", file=fout)

editorlengths = [0] * len(arrayofmistakes)
for i in range(len(arrayofmistakes)):  # задание 5
    # выводим полученные результаты, исправляя ошибку функции, вызванную +2 для пропуска анаграмм
    if changers[i] != "не найдено":
        if editorlen(arrayofmistakes[i], changers[i]) == 2:
            editorlengths[i] = 1
        elif editorlen(arrayofmistakes[i], changers[i]) == 0:
            editorlengths[i] = 2
        else:
            editorlengths[i] = editorlen(arrayofmistakes[i], changers[i])
        print(arrayofmistakes[i], changers[i], editorlengths[i], file=fout)
    else:
        print(arrayofmistakes[i], changers[i], file=fout)

print(' '.join(text), file=fout1)
fin.close()
