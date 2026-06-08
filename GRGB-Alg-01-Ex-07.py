def func2(number):
    listdiv = []
    div = number
    sum = 0
    while div > 0:
        if number % div == 0:
            listdiv.append(div)
        div = div - 1
    for i in range(len(listdiv)):
        sum = sum + listdiv[i]
    if sum == number*2:
        print("yes")
    else:
        print("no")

number = int(input())
func2(number)

def main(proceed):
    proceed = input("testar main? (1 ou 0)")
    if proceed == "1":
        for i in range(1, 10000):
            listdiv = []
            number = i
            div = number
            sum = 0
            while div > 0:
                if number % div == 0:
                    listdiv.append(div)
                div = div - 1
            for i in range(len(listdiv)):
                sum = sum + listdiv[i]
            if sum == number*2:
                print(number)
        
main(func2)