n = int(input("Digite um numero inteiro positivo. \n"))

#fiz apenas pra ver como if funciona no python, faz tempo q n faco nesta linguagem
if n <= 0:
    print("O numero deve ser um inteiro positivo. \n")

else:
    soma = (n * (n + 1)) // 2
    
print(f"A soma dos números inteiros de 1 a {n} e: {soma}")
