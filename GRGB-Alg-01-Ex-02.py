def func(string1, string2):
    num1 = set()
    num2 = set()
    num3 = set()

    for number in string1:
        num1.add(number)
    for number in string2:
        num2.add(number)
    
    for number in num1:
        if number not in num2:
            num3.add(number)
    for number in num2:
        if number not in num1:
            num3.add(number)
    
    return num3

def main():
    string1 = input()
    string2 = input()

    result = func(string1, string2)

    for number in result:
        print(number)

main()