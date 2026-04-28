#cesar's encrption

text = input()
shift = int(input())
result = ""

while True:

    if text == "":
        break

    for char in text:

        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)

        # base: determina em que caixa a letra esta e associa o unicode de acordo
        # chr: converte o unicode de volta para caractere
        # ord: converte o caractere para unicode
        # (ord(char) - base + shift) % 26: calcula a posiçao da letra apos o deslocamento, garantindo que ela permaneça dentro do alfabeto
        # + base: converte a posiçao de volta para o codigo unicode correspondente a letra maiuscula ou minuscula
        # importante para dps !!!

        else:
            result += char

    print(result)
    result = ""
    text = input()