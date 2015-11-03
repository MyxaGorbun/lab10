input = open('input.txt', 'r')
a = input.readlines()
b = ''
for s in a:
    s = s.rstrip()
    s.replace('.', '')
    s.replace(',', '')
    s.replace('?', '')
    s.replace('!', '')
    b += ' '
    b += s
b = b.split()
for l in b:
    l.lower()
c = list(set(b))
wton = dict()
ntow = dict()
for x in c:
    wton[x] = b.count(x)
for key in wton:
    if wton.get(key) in ntow:
        e = ntow[wton.get(key)] + key
        ntow[wton.get(key)] = e
    else:
        ntow[wton.get(key)] = key
w = list(ntow.keys())
for q in w:
    q = int(q)
q = max(w)
q = ntow[q]
print(q)