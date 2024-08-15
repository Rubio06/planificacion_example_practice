import pandas as pd
import json
import os
from xlsxwriter import Workbook

# Crear DataFrames de ejemplo
df = pd.DataFrame({
    'Nombre': ['Juan', 'Ana', 'Luis'],
    'Apellido': ['Rubio', 'Carlosne', 'Ternero'],
    'Edad': [28, 24, 35],
})

df2 = pd.DataFrame({
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia'],
    'País': ['España', 'España', 'España'],
    'Población': [3200000, 1600000, 800000],
})

df3 = pd.DataFrame({
    'Comandos': ['f2', 'f3'],
    'Review': ['m5', 'm6']
})

# Convertir DataFrames a JSON (como una lista de diccionarios)
df_json = df.to_dict(orient='records')
df2_json = df2.to_dict(orient='records')
df3_json = df3.to_dict(orient='records')

# Crear archivo para guardar el JSON
output_dir = 'result_data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Guardar en un archivo JSON
output_file_json = os.path.join(output_dir, "data.json")
with open(output_file_json, 'w', encoding='UTF-8') as f:
    json.dump({'tabla1': df_json, 'tabla2': df2_json, 'tabla3': df3_json}, f, indent=4)

# Ubicando el archivo Excel para su creación
output_file_excel = os.path.join(output_dir, "result.xlsx")

with pd.ExcelWriter(output_file_excel, engine='xlsxwriter') as writer:
    # Crear una hoja con el nombre 'Hoja creada'
    worksheet = writer.book.add_worksheet('Hoja creada')
    
    # Definir formatos para los encabezados, celdas de datos y celdas combinadas
    header_format = writer.book.add_format({
        'bold': True,
        'font_size': 12,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#D7E4BC',
        'border': 1
    })
    
    cell_format = writer.book.add_format({
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
    })
    
    merge_format = writer.book.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter',
    })
    
    start_col = 1  # La columna B corresponde al índice 1

    # Ejemplo de combinar celdas para el título
    worksheet.merge_range(0, 1, 0, 6, 'Título Combinado', merge_format)
    
    ### PRIMERA TABLA

    # Escribir encabezados de la primera tabla
    for col_num, value in enumerate(df.columns):
        col_start = start_col + col_num * 2  # Columna inicial para encabezado
        col_end = col_start + 1  # Columna final para encabezado
        worksheet.merge_range(2, col_start, 2, col_end, value, header_format)

    # Escribir los datos del DataFrame en el Excel y combinar celdas
    for row_num, record in enumerate(df_json, start=3):
        for col_num, key in enumerate(df.columns):
            col_start = start_col + col_num * 2  # Columna inicial para datos
            col_end = col_start + 1  # Columna final para datos
            worksheet.merge_range(row_num, col_start, row_num, col_end, record[key], cell_format)

    ### SEGUNDA TABLA

    # Definir la columna de inicio para la segunda tabla
    start_col2 = start_col + len(df.columns) * 2 + 2  # Dejar un espacio entre tablas

    # Escribir encabezados de la segunda tabla
    for col_num, value in enumerate(df2.columns):
        col_start = start_col2 + col_num * 2  # Columna inicial para encabezado
        col_end = col_start + 1  # Columna final para encabezado
        worksheet.merge_range(2, col_start, 2, col_end, value, header_format)

    # Escribir los datos del segundo DataFrame en el Excel y combinar celdas
    for row_num, record in enumerate(df2_json, start=3):
        for col_num, key in enumerate(df2.columns):
            col_start = start_col2 + col_num * 2  # Columna inicial para datos
            col_end = col_start + 1  # Columna final para datos
            worksheet.merge_range(row_num, col_start, row_num, col_end, record[key], cell_format)
    
    ### TERCERA TABLA

    # Definir la fila de inicio para la tercera tabla, debajo de la primera tabla
    start_row3 = len(df_json) + 5  # 5 filas de separación después de la primera tabla

    # Escribir encabezados de la tercera tabla
    for col_num, value in enumerate(df3.columns):
        col_start = start_col + col_num * 2  # Columna inicial para encabezado
        col_end = col_start + 1  # Columna final para encabezado
        worksheet.merge_range(start_row3, col_start + 2, start_row3, col_end + 2, value, header_format)

    # Escribir los datos del tercer DataFrame en el Excel y combinar celdas
    for row_num, record in enumerate(df3_json, start=start_row3 + 1):
        for col_num, key in enumerate(df3.columns):
            col_start = start_col + col_num * 2  # Columna inicial para datos
            col_end = col_start + 1  # Columna final para datos
            worksheet.merge_range(row_num, col_start + 2, row_num, col_end + 2, record[key], cell_format)
            

            
    print(len(df_json))
    print(start_row3)
    
    

print(f'Archivo JSON guardado correctamente en {output_file_json}')
print(f'Archivo Excel guardado correctamente en {output_file_excel}')
