
# data = [12,22]

# [doce, veintidos] = data
# print(doce)

cadena_1 = "Hola como estas"
cadena_2 = "22"
cadena_3 = "el resultado no existe"

result_1 = len(cadena_1)
result_2 = cadena_2.isnumeric()
result_3 = cadena_3.capitalize()
print(result_1)
print(result_2)
print(result_3)


numero_encontrar = lambda x: x + 12


print(numero_encontrar(2))