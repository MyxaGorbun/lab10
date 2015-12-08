dictionary = open('en-ru1.txt', 'rw')
ruen = open('ru-en1.txt', 'rw')
Enru = {}
a = dictionary.readline()
while a != '':
    a.replace(' ', '\t')
    a = a.split('\t-\t')
    Enru[a[1].strip()] = a[0].strip()
    a = dictionary.readline()
Ruen = {}
a = ruen.readline()
while a != '':
    a.replace(' ', '\t')
    a = a.split('\t-\t')
    Ruen[a[1].strip()] = a[0].strip()
    a = dictionary.readline()
for key in Ruen:
    if Ruen[key] in Enru:
        Enru[Ruen[key]] = Enru[Ruen[key]] + ',' + str(key)
    else:
        Enru[Ruen[key]] = str(key)
for key in Enru:
    if Enru[key] in Ruen:
        Ruen[Enru[key]] = Ruen[Enru[key]] + ',' + str(key)
    else:
        Ruen[Enru[key]] = str(key)
for key in Enru:
    print(key, '\t-\t', Enru[key], file=dictionary)
for key in Ruen:
    print(key, '\t-\t', Ruen[key], file=ruen)