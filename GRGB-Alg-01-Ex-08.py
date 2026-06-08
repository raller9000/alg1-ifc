def main():
    stringos = input()
    stringossplit = stringos.split()
    stringoslist = []
    for i in range(len(stringossplit)):
        if stringossplit[i] != "":
            stringoslist.append(stringossplit[i])
    print(stringoslist)

main()