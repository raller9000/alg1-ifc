lista1 = []

while True:
    number = input()
    if number == '':
        break
    lista1.append(int(number))

lista1.sort()

for number in lista1:
    print(number)
