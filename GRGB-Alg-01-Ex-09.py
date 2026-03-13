firstDepo = float(input("Digite o valor do primeiro depósito. \n"))

#pelo que eu entendo uma variavel estatica taxa é mais facilde usar e facilita ter em um projeto maior
tax = 0.12

firstYear = firstDepo + (firstDepo * tax)
secondYear = firstYear + (firstYear * tax)
thirdYear = secondYear + (secondYear * tax)

print(f"valor do primeiro ano: R$ {firstYear:.2f} \nvalor do segundo ano: R$ {secondYear:.2f} \nvalor do terceiro ano: R$ {thirdYear:.2f} \n")