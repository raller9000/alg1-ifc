x = float(input("Quantas bugigangas? \n"))
y = float(input("Quantas quinquilharias? \n"))

# EU COLOCAR VARIAVEL EM INGLES SIM, é costume, da pra ver nos outros projetos no meu git :)
floattokilo = (x * 75) + (y * 112) / 1000
total = x + y

print(f"Total de itens: {total} \nTotal em kg: {floattokilo:.2f} \n")
