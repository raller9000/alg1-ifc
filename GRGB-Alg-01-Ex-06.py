number = int(input())

def main():
    listdiv = []
    div = number
    while div > 0:
        if number % div == 0:
            listdiv.append(div)
        div = div - 1
    print(listdiv)

main()