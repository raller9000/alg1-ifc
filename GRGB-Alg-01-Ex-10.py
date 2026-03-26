matricula = input("Digite uma matricula (AASDDD) \n")

if len(matricula) == 6 and matricula.isdigit():
    ano = str(matricula[0:2])
    semestre = str(matricula[2:3])
    id = str(matricula[3:6])
    
    print("ano da matricula:", ano, "\nsemestre da matricula:", semestre)