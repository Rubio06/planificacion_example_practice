import math 
import numpy as np

def calculate_ideal_size(days, last_sales_day, tvu, remove_product, sizes):
    def ideal_size_product(days, last_sales_day, tvu, remove_product):
        return math.trunc((last_sales_day / days) * (tvu - remove_product))

    ideal_size = ideal_size_product(days, last_sales_day, tvu, remove_product)
    min_size = min(sizes)
    percentile_25 = np.percentile(sizes, 25)
    return ideal_size, min_size, percentile_25

# Ejemplo de uso
days = 28
last_sales_day = int(input("Ingrese la venta de los últimos días: "))
tvu = 60
remove_product = 7
sizes = [10, 15, 12, 18, 20]

# Llamar a la función para calcular todo
ideal_size, min_size, percentile_25 = calculate_ideal_size(days, last_sales_day, tvu, remove_product, sizes)

# Mostrar resultados
print(f"Tamaño ideal calculado para un SKU: {ideal_size}")
print(f"Tamaño ideal mínimo de todos los casos: {min_size}")
print(f"Tamaño ideal mínimo que abarca el percentil 25: {percentile_25}")