
def evaluate_inerpack(ddi_innerpack, tvu, stock, last_sales_day):
    if ddi_innerpack <= tvu:
        return "OK"
    elif stock == 0 and last_sales_day == 0:
        return "PRODUCTO SIN CARGA"
    elif stock > 0 and last_sales_day == 0:
        return "PRODUCTO SIN VENTA"
    else:
        return "BAJAR PACKQTY"
    
# Ejemplo de uso
while True:
    try:
        ddi_innerpack = float(input("Ingrese el dato de ddi_innerpack: "))
        
        if isinstance(ddi_innerpack, str):
            print("Usted a elegido un texto")
            
        tvu = float(input("Ingrese el dato de tvu: "))
        stock = int(input("Ingrese el dato de stock: "))
        last_sales_day = int(input("Ingrese la venta de los últimos días: "))
        resultado = evaluate_inerpack(ddi_innerpack, tvu, stock, last_sales_day)
        print(f"Resultado: {resultado}")
    
    except ValueError:
        print("Es un valor")

