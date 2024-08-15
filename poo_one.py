class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        if self.grado == 1:
            print("Tiene un grado resptable")
        elif self.grado == 2:
            print("Tienes buen grado")    
        elif self.grado == 3:
            print("Tu grado no es suficiente")
    
    def addMessage(self):
        return f"el nombre es {self.nombre} la edad es {self.edad} el grado es {self.grado}"
    
    def addData(self):
        ## archivo_sin_leer = open("archivos\\archivo_example.txt")    
        ## archivo = archivo_sin_leer.read()
        # Supongamos que estás dentro de una clase y self.nombre, self.edad y self.grado están definidos
        texto = f"el nombre es {self.nombre}, la edad es {self.edad} y el grado es {self.grado}"

        # Escribir en el archivo
        with open('archivos/archivo_example.txt', 'w') as archivo:
            archivo.write(texto)

        # Leer el archivo y imprimir su contenido
        with open('archivos/archivo_example.txt', 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
                    
while True:
    try: 
        nombre = input("Digame su nombre: ")        
        edad = input("Digame su edad: ")        
        grado = int(input("Digame su grado: "))        

        estudiante = Estudiante(nombre, edad, grado)
        print(f""" 
            DATOS DEL ESTUDIANTE \n\n
            Nombre: {estudiante.nombre} \n
            Edad: {estudiante.edad} \n
            Grado: {estudiante.grado} \n
            """)
        
        estudiante.addMessage()
        estudiante.estudiar()
        estudiante.addData()
    except ValueError:
        print("error de tipo de dato")
        break
        





