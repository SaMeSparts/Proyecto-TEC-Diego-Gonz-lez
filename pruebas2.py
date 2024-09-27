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
            print(f"la cuenta {contraseña} ha sido agregada")
    
    def mostrar_contraseñas(self):
        return self.contraseña

            
gestor_cuentas=Gestor_cuentas()
gestor_contraseñas=Gestor_contraseñas()
print(gestor_cuentas.mostrar_cuentas())



while cuenta_num==0:
    pregunta_cuenta=str(input("Tienes cuenta o eres nuevo?(cuenta)(nuevo)\n"))
    if pregunta_cuenta.lower()=="cuenta":
        desicion_usuario=str(input("Usuario o Admin\n"))

        if desicion_usuario.lower()=="usuario":                
            cuenta=str(input("Escribe tu cuenta?\n"))
            if cuenta in gestor_cuentas.__init__():
                print("Cual es la contraseña:\n")

        if desicion_usuario.lower()=="admin":                    
            cuenta=str(input("Escribe tu cuenta?\n"))
            if cuenta in gestor_cuentas.__init__():
                print("Cual es la contraseña:\n")
        
    
    elif pregunta_cuenta.lower()=="nuevo":
        cuenta_nueva=str(input("Escribe el nombre de tu nueva cuenta?\n"))
        gestor_cuentas.agregar_cuenta(cuenta_nueva)
        contraseña_nueva=str(input("Escribe la contraseña\n"))
        gestor_contraseñas.agregar_contraseña(contraseña_nueva)
    else:
        print("escribe correctamente: ")