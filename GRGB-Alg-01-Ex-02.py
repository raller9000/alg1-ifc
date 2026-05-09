#imprime_n_vezes(nome, n)

def imprime_n_vezes(nome, n):
    nome = input()
    n = int(input())

    while n > 0:
        print(nome)
        n = n - 1

imprime_n_vezes()

