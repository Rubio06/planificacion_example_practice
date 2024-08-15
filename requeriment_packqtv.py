def get_data(message: str, date_type):
    while True:
        try:
            if date_type == float:
                return float(input(message))
            elif date_type == int:
                return int(input(message))
            elif date_type == str:
                return str(input(message))
            else:
                raise ValueError("Tipo de dato no soportado")
        except ValueError:
            print(f"Error: Debes ingresar un dato de tipo {date_type.__name__}")

def evaluate_packqty(ddi_packqty, tvu, stock, last_sales_day):
    if ddi_packqty <= tvu:
        return 'OK'
    elif stock == 0 and last_sales_day == 0:
        return 'PRODUCTO SIN CARGA'
    elif stock > 0 and last_sales_day == 0:
        return 'PRODUCTO SIN VENTA'
    else:
        return 'BAJAR PACKQTY'

ddi_packqty: float = get_data("Ingresar el dato de ddi_packqty: ", float)
tvu: int = get_data("Ingresar el dato de tvu: ", int)
stock: int = get_data("Ingresar el dato de stock: ", int)
last_sales_day: int = get_data("Ingresar el dato de VtaUltDiasCant: ", int)

validate_packqty: str = evaluate_packqty(ddi_packqty, tvu, stock, last_sales_day)
print(f"El resultado es: { validate_packqty }")



        
        
    







    
        