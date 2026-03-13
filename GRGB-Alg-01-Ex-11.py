import math

longitude = float(input("Digite a longitude em graus. \n"))
latitude = float(input("Digite a latitude em graus. \n"))
 
longitudeRad = math.radians(longitude)
latitudeRad = math.radians(latitude)

# distancia = 6371.01 × arccos(sen(t1) × sen(t2) + cos(t1) × cos(t2) × cos(g1 − g2)) do exercicio

distance = 6371.01 * (2 * ((latitudeRad - 0) / 2) ** 2 + (longitudeRad - 0) / 2 ** 2) ** (1 / 2)
distancekm = distance * 1000

# pelo que entendi isso é em relacao a um ponto 0,0 ?

print(f"A distancia do ponto 0,0 e: {distance:.2f} km \n")

# eu também fiz usando uma tranformação manual pra radianos usando:
# longitudeRad = longitude * (math.pi / 180)
# latitudeRad = latitude * (math.pi / 180)
# porem o resultado teve uma margem de 1km de diferenca, porque?