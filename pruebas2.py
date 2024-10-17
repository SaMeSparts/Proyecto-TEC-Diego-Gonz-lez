cuenta_num=0

class Gestor_cuentas:
    def __init__(self):
        # Leer cuentas desde el archivo al iniciar
        try:
            with open("cuentas.txt", "r") as f:
                self.cuentas = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.cuentas = []

    def agregar_cuenta(self, cuenta):
        if cuenta in self.cuentas:
            print("Esta cuenta ya existe \n")
        else:
            self.cuentas.append(cuenta)
            with open("cuentas.txt", "a") as f:
                f.write(cuenta + "\n")
            print(f"La cuenta {cuenta} ha sido agregada")

    def mostrar_cuentas(self):
        return self.cuentas


class Gestor_contraseñas:
    def __init__(self):
        # Leer contraseñas desde el archivo al iniciar
        try:
            with open("contraseñas.txt", "r") as f:
                self.contraseñas = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            self.contraseñas = []

    def agregar_contraseña(self, contraseña):
        if contraseña in self.contraseñas:
            print("Esta contraseña ya existe \n")
        else:
            self.contraseñas.append(contraseña)
            with open("contraseñas.txt", "a") as f:
                f.write(contraseña + "\n")
            print(f"La contraseña {contraseña} ha sido agregada")

    def mostrar_contraseñas(self):
        return self.contraseñas


gestor_cuentas = Gestor_cuentas()
gestor_contraseñas = Gestor_contraseñas()
print("Cuentas disponibles: ", gestor_cuentas.mostrar_cuentas())

while cuenta_num == 0:
    pregunta_cuenta = str(input("¿Tienes cuenta o eres nuevo? (cuenta/nuevo)\n"))
    
    if pregunta_cuenta.lower() == "cuenta":
        desicion_usuario = str(input("¿Usuario o Admin?\n"))

        if desicion_usuario.lower() in ["usuario", "admin"]:
            cuenta = str(input("Escribe tu cuenta:\n"))
            if cuenta in gestor_cuentas.mostrar_cuentas():
                contraseña = str(input("Escribe tu contraseña:\n"))
                if contraseña in gestor_contraseñas.mostrar_contraseñas():
                    print("Inicio de sesión exitoso")
                    cuenta_num += 1
                else:
                    print("Contraseña incorrecta")
            else:
                print("La cuenta no existe")
    
    elif pregunta_cuenta.lower() == "nuevo":
        cuenta_nueva = str(input("Escribe el nombre de tu nueva cuenta:\n"))
        gestor_cuentas.agregar_cuenta(cuenta_nueva)
        
        contraseña_nueva = str(input("Escribe la nueva contraseña:\n"))
        gestor_contraseñas.agregar_contraseña(contraseña_nueva)
        
        print("Cuenta y contraseña creadas exitosamente.")
        cuenta_num += 1
    
    else:
        print("Escribe correctamente.")
