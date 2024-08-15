import pandas as pd

# Definir las columnas
columns = ['ID', 'NOMBRE', 'APELLIDO']
array_list = []

# Pedir al usuario el número de filas que desea agregar
num_rows = int(input('Cuántas filas deseas agregar a tu excel: '))

# Recoger los datos del usuario
for i in range(num_rows):
    row = []
    for column in columns:
        value = input(f'Ingrese la columna {column}: ')
        row.append(value)
        
    array_list.append(row)

# Crear el DataFrame
df = pd.DataFrame(array_list, columns=columns)

# Nombre del archivo de salida
output_excel = 'EXCEL_PRACTICE_RESULT.xlsx'

# Escribir el DataFrame en el archivo Excel
with pd.ExcelWriter(output_excel, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='Resultado practice', index=False, startrow=2, startcol=2)

    # Obtener la hoja del Excel
    worksheet = writer.sheets['Resultado practice']
    
    # Definir formatos
    header_format = writer.book.add_format({
        'border': 1,
        'align': 'center',
    })

    color_cell = writer.book.add_format({
        'align': 'center',
        'bg_color': '#FFFF00'  # Ejemplo: color amarillo de fondo
    })

    # Agregar formato a todos los registros sin contar los encabezados
    start_col_name = "ID"
    end_col_name = "APELLIDO"
    
    start_col_index = df.columns.get_loc(start_col_name)
    end_col_index = df.columns.get_loc(end_col_name)
    
    start_row = 2 
    end_row = start_row + len(df) - 1

    for col_num in range(start_col_index, end_col_index + 1):
        for row_num in range(start_row, end_row + 1):
            worksheet.write(row_num + 1, col_num + 2, df.iloc[row_num - start_row, col_num], header_format)

    # Agregar un color a una celda específica
    worksheet.write(3, 4, df.iloc[0, 2], color_cell)  # Nota: Índices basados en 0

    # Agregar ancho a la columna "APELLIDO"
    # col_ProveeNombre = df.columns.get_loc('APELLIDO') + 2  # Ajustar el índice de la columna
    # worksheet.set_column(col_ProveeNombre, col_ProveeNombre, 35)
    
    # for row_num in range(start_row, end_row + 1):
    #     worksheet.write(row_num + 1, col_ProveeNombre, df.iloc[row_num - start_row, col_ProveeNombre - 2], header_format)

print(f'Datos escritos en {output_excel}')
