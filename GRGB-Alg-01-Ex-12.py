#table of multiplication with while

column = 1
row = 1

while row <= 10:
    while column <= 10:
        print(row * column, end="\t")
        column += 1
    print()
    row += 1
    column = 1