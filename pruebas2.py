cuentas=["A01713489"]
cuenta_num=0
cuenta_num2=0
cuenta_num3=0
cuenta_num4=0


class Gestor_cuentas:
    def __init__(self):
        self.cuentas=[]

    def agregar_cuenta(self,cuenta):
        if cuenta in self.cuentas:
            print("Esta cuenta ya existe \n")
        else:
            self.cuentas.append(cuenta)
            print(f"la cuenta {cuenta} ha sido agregada")

    def mostrar_cuentas(self):
        return self.cuentas

        
class Gestor_contraseñas:
    def __init__(self):
        self.contraseña=[]

    def agregar_contraseña(self,contraseña):
        if contraseña in self.contraseña:
            print("esta contraseña ya existe \n")
        else:
            self.contraseña.append(contraseña)
            print(f"la cuenta {cuenta} ha sido agregada")
    
    def mostrar_contraseñas(self):
        return self.contraseña

            
gestor_cuentas=Gestor_cuentas()
gestor_contraseñas=Gestor_cuentas()



while cuenta_num==0:
    pregunta_cuenta=str(input("Tienes cuenta o eres nuevo?(cuenta)(nuevo)\n"))
    if pregunta_cuenta.lower()=="cuenta":
        cuenta=str(input("Escribe es tu cuenta?\n"))

        if cuenta in gestor_cuentas.__init__():
            print("Cual es la contraseña:\n")

    
    elif pregunta_cuenta.lower()=="nuevo":
        cuenta_nueva=str(input("Escribe el nombre de tu nueva cuenta?\n"))
        

    else:
        print("escribe correctamente: ")