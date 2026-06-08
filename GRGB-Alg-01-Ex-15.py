def precedencia(stringos):
    if stringos == "+" or stringos == "-":
        return 1
    elif stringos == "*" or stringos == "/":
        return 2
    elif stringos == "^":
        return 3
    else:
        return -1
    
def main():
    stringos = input()
    print(precedencia(stringos))
main()