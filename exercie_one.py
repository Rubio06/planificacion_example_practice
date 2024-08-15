# creando un entorno virtual
# python -m venv env
# env\Scripts\activate
# pip install openpyxl
import pandas as pd

inputs_col = [2,3,4,5,6,7,8]
df = pd.read_excel('archivos/UMP_PROV487_20240604.xlsx', 
                   sheet_name='Validación',
                   header = 1, 
                   usecols = inputs_col)

# contando la cantidad de columnas y filas
print(df.shape)



# numero de columnas
print(df.columns)

# muestra la cantidad filas que es 5
print(df.head(5))

# muestra las ultimas 5 filas
print(df.tail(5))






# df = df[df["DistNombre"] == "COMAS"]

# df_cols = df.columns

# for col in df_cols:
#     print(df[col].head(5))

# # OBTENIENDO LOS 5 PRIMEROS REGISTROS
# print(df['IdProducto'].head(5))


