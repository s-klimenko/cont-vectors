
'''
POS = ('S', 'A', 'NUM', 'A-NUM', 'V', 'ADV', 'PRAEDIC', 'PARENTH', 'S-PRO', 'A-PRO', 'ADV-PRO', 'PRAEDIC-PRO', 'PR', 'CONJ', 'PART', 'INTJ')
num = ('-2','-1','+1','+2', '+3', '+4')
dict = {'name':[]}
voc = {'name':'a', 'V_-2':5, 'SPRO_-1':1, 'ADV_+3':2, 'ADV_-2':2, 'S_+4':7, 'CONJ_+2':1}
voc2 = {'S_+3':13, 'CONJ_+4':1, 'S_-2':8, 'ADV_+3':3, 'ADV_-2':4,  'бойко_+2':1, 'disamb_+3':1, 'PR_+4':2, 'ADV_+2':5, 'V_+1':23, 'APRO_+2':2, 'PR_+2':3, 'CONJ_-2':3, 'disamb_+4':1, 'PART_-1':2, 'CONJ_-1':2, 'A_+3':2, 'PART_+2':2, 'name':'b'}
for i in POS:
    for j in num:
        k = i + '_' + j
        dict[k] = []

for i in dict:
    if i not in voc:
        voc[i] = 0
print(voc)
'''
a = []
for r in range(6): # 6 строк
    a.append([]) # создаем пустую строку
print(a)
