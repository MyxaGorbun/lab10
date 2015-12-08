dictionary = open('en-ru.txt', 'r')
Words = {'the':''}
a = dictionary.readline()
while a != '':
    a.replace(' ', '\t')
    a = a.split('\t-\t')
    Words[a[0].strip()] = a[1].strip()
    a = dictionary.readline()
input = open('input.txt', 'r')
output = open('output.txt', 'w')
a = input.read()
a = a.split()
for i in range(len(a)):
    a[i] = a[i].replace('.', '\t')
    a[i] = a[i].replace(',', '\t')
    a[i] = a[i].replace('!', '\t')
    a[i] = a[i].replace('?', '\t')
    a[i] = a[i].replace(';', '\t')
    a[i] = a[i].replace(':', '\t')
    a[i] = a[i].replace('-', '\t')
    a[i] = a[i].replace('/', '\t')
    a[i] = a[i].replace('\'', '\t')
    a[i] = a[i].strip()
    a[i] = a[i].lower()
    if a[i] in Words:
        a[i] = Words[a[i]]
for i in range(len(a)):
    print(a[i], file=output, end=' ')