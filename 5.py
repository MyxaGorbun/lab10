dictionary = open('en-ru.txt', 'r')
ruen = open('ru-en.txt', 'w')
Words = {}
a = dictionary.readline()
while a != '':
    a.replace(' ', '\t')
    a = a.split('\t-\t')
    Words[a[1].strip()] = a[0].strip()
    a = dictionary.readline()
W = []
for key in Words:
    W.append(str(key) + '\t-\t' + str(Words[key]))
    W.sort()
for i in range(len(W)):
    print(W[i], file=ruen)