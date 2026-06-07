lista1 = []

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

def main():
    lista1 = []    
    while True:
        numero = int(input())
    
        if numero == 0:
            break
        if len(str(abs(numero))) < 4:
            messagebox.showerror("Valor inválido", "O número deve conter no máximo 4 dígitos.")
            break

        lista1.append(numero)
    
    x = len(lista1)
    lista1 = sorted(lista1)
    lista2 = []

    for i in range(2, x-2):
        lista2.append(lista1[i])

    print(lista2)
    print(lista1)

main()
