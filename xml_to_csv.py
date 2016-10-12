import re
import os
import csv

def big_dict():
    POS = ('S', 'A', 'NUM', 'ANUM', 'V', 'ADV', 'PRAEDIC', 'PARENTH', 'SPRO', 'APRO', 'ADVPRO', 'PRAEDICPRO', 'PR', 'CONJ', 'PART', 'INTJ')
    num = ('-2','-1','+1','+2', '+3', '+4')
    dict = {'name':''}
    for i in POS:
        for j in num:
            k = i + '_' + j
            dict[k] = ''
    return dict

def file_to_string(file_name, word):
    j = open (file_name,'r', encoding = 'utf-8')
    f = j.read()
    result = re.findall('<ana lex="(.*?)"|(</snippet>)|gramm="([A-Za-z\-\|]*?) ', f) #находит все лексемы, слова и сниппеты
    big_list = []
    all_lists = []
    list = []
    for i in result: #обрезает пустые значения и делает длинный список big_list со всем нужным
        for j in i:
            if j != '':
                big_list.append(j)
    for i in range(len(big_list)): #разделяет список на подсписки по сниппетам,/
        #  приводит список ['A', 'a', 'C' 'c', 'X', 'x', 'D', 'd'], /
        # где теги строчные буквы, а искомое слово Х, к виду ['a', 'c', 'X', 'd']
        if big_list[i] == '</snippet>':
            all_lists.append(list)
            list = []
        if big_list[i] != word and big_list[i] != '</snippet>' and re.match('[A-Za-z]', big_list[i]) == None and re.match('[A-Za-z]', big_list[i+1]) != None:
            list.append(big_list[i+1])
        if big_list[i] == word:
            list.append(big_list[i])
    return all_lists

def string_into_vocabulary(string, X): #берет строку типа ['a', 'b', 'c', 'X', 'd', 'e', 'f', 'g'], /
    # возвращает словарь с нумерацией слева и справа от X
    n = 0
    m = 0
    for i in string:
        if i != X:
            n += 1
        else:
            m = n
            break
    for i in string[:n]:
        token = str(i) + '_-' + str(n)
        try:
            voc[token] += 1
        except:
            voc[token] = 1
        n -= 1
    n += 1
    for i in string[m+1:]:
        token = str(i) + '_+' + str(n)
        try:
            voc[token] += 1
        except:
            voc[token] = 1
        n += 1

def string_into_vocabulary_stripped(string, X): #берет строку типа ['a', 'b', 'c', 'X', 'd', 'e', 'f', 'g'], /
    # возвращает словарь с нумерацией слева и справа от X
    # !!! НЕ ВИДИТ ВТОРОГО СЛОВА, ЕСЛИ ОНО ПОВТОРЯЕТСЯ, ПОПРАВЬ
    n = 0
    m = 0
    for i in string:
        if i != X:
            n += 1
        else:
            m = n
            break
    for i in string[:n]:
        if n <= 2:
            token = str(i) + '_-' + str(n)
            try:
                voc[token] += 1
            except:
                voc[token] = 1
            n -= 1
    n += 1
    for i in string[m+1:]:
        if n <= 4:
            token = str(i) + '_+' + str(n)
            try:
                voc[token] += 1
            except:
                voc[token] = 1
            n += 1

big_dictionary = big_dict() #список частей речи
big_dictionary['name'] = ''

n = 0 #пронумерованный список частей речи
for i in big_dictionary:
    big_dictionary[i] = n
    n += 1

table = [] #итоговая таблица
for r in range(len(big_dictionary)):
    table.append([])

for i in big_dictionary: #добавляю в таблицу части речи под номерами
    num = big_dictionary[i]
    table[num].append(i)

for root, dirs, files in os.walk ('.\\1'):
    for fname in files:
        fullpath = '.\\1\\' + fname
        lex = fname.strip('.xml')
        if fname.strip('.xml') == 'быстрее' or fname.strip('.xml') == 'быстрей' or fname.strip('.xml') ==  'побыстрее' or fname.strip('.xml') ==  'побыстрей':
            word = 'быстро'
        elif fname.strip('.xml') == 'медленнее' or fname.strip('.xml') == 'медленней' or fname.strip('.xml') == 'помедленней' or fname.strip('.xml') == 'помедленнее':
            word = 'медленно'
        elif fname.strip('.xml') == 'скорее' or fname.strip('.xml') == 'скорей' or fname.strip('.xml') == 'поскорей' or fname.strip('.xml') == 'поскорее':
            word = 'скоро'
        else:
            word = lex
        all_lists_final = file_to_string(fullpath, word)
        voc = {}
        voc['name'] = lex
        for token in all_lists_final:
            string_into_vocabulary_stripped(token, word)
        for i in big_dictionary: # если слово не встретилось в             if i not in voc:
                voc[i] = 0
        for m in voc:
            if m in big_dictionary:
                num = big_dictionary[m]
                table[num].append(voc[m])

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(table)

