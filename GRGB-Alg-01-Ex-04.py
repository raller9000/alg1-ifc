lista1 = []

while True:
    word = input()
    if word == '':
        break
    lista1.append(word)

for word in lista1:
    N = lista1.count(word)
    while N != 1:
        lista1.remove(word)
        N = lista1.count(word)

print(lista1)