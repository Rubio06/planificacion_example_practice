class Login():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def EnterSystem(self):
        if self.username == "" or self.password == "":
            print("Los campos estan vacios intente de nuevo")
            return False
        else:
            if self.username == "Enoc20" or self.password == "12345":
                print("Ingreso correctamente")
                return True
            else:
                print("Los datos son incorrectos ingrese nuevo")
                return False
            
    def RegisterSystem():
        
        return 
        

condition: bool = True

while condition:
    print("-------------------------------")
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su password: ")
            
    # INSTANCIAS DE CLASE
    print("-------------------------------")
    user_one = Login(username, password)
    condition = not user_one.EnterSystem()  # Actualiza condition basado en la respuesta de EnterSystem


        


