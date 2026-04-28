#sales

price = [4.95, 9.95, 14.95, 19.95, 24.95] 
disconto = 0.20

i = 0

print("Original\tCom Desconto")

while i < 5:
    original = price[i]
    discontado = original * (1 - disconto)
    
    print(f"{original:.2f}\t\t{discontado:.2f}")
    
    i += 1