texto = input("Ingrese una palabra: ").lower()
inverso = texto[::-1]
if texto == inverso:
    print("La palabra ingresada si es palindromo")
else:
    print("La palabra ingresada no es palindromo")


