import math 
import random
import os

lista_materiales_grupos="materiales estucturales, materiales acabado, materiales aislantes,\n materiales unionyadhesivos, materiales instalaciones, materiales naturales,\n materiales recubrimiento"
materiales_estucturales={"Hormigon":80,"Acero":1,"Madera":400,"Ladrillo":0.30,"Piedra":50,"Aluminio":2}
materiales_acabado={"Yeso":0.30,"Vidrio":20,"Tejas":0.50,"Pintura":10,"Baldosas":50,"Papel Pintado":4}
materiales_aislantes={"Lana Mineral":80,"Espuma de poliuretano":10,"Poliestireno expandido":5,"Corcho:":15}
materiales_unionyadhesivos={"Cemento":8,"Mortero":5,"Siliconas":4,"Resinas epoxi":20}
materiales_instalaciones={"Cobre":8,"PVC":1,"Polipropileno":4,"Acero galvanizado":3,}
materiales_naturales={"Madera":400,"Bambú":1,"Adobe":0.10,"Piedra":50}
materiales_recubrimiento={"Enyesado":6,"Pladur":10,"Azulejos":25,"Mármol":100}
lista_materiales= materiales_estucturales, materiales_acabado, materiales_aislantes, materiales_unionyadhesivos, materiales_instalaciones, materiales_naturales, materiales_recubrimiento




saldo_cliente="saldocliente.txt"
saldo_empresa="saldoempresa.txt"
cantidad_pago_total=0
repeticion=0

def leer_saldo_cliente():
    if os.path.exists(saldo_cliente):
        with open(saldo_cliente, "r") as archivo_saldo_cliente:
            return float(archivo_saldo_cliente.read().strip())
    else: return 0.0
def leer_saldo_empresa():
    if os.path.exists(saldo_empresa):
        with open(saldo_empresa, "r") as archivo_saldo_empresa:
            return float(archivo_saldo_empresa.read().strip())
    else: return 0.0
def escribir_saldo_cliente(saldo):
    with open(saldo_cliente, "w") as archivo_saldo_cliente:
        archivo_saldo_cliente.write(str(saldo))
def escribir_saldo_empresa(saldo2):
    with open(saldo_empresa, "w") as archivo_saldo_empresa:
        archivo_saldo_empresa.write(str(saldo2))
def agregar_saldo_cliente(cantidad):
    saldo = leer_saldo_cliente()
    saldo += cantidad
    escribir_saldo_cliente(saldo)
    print(f"Se han agregado {cantidad:.2f} unidades. Saldo actual: {saldo:.2f}\n")
def agregar_saldo_empresa(cantidad2):
    saldo2 = leer_saldo_empresa()
    saldo2 += cantidad2
    escribir_saldo_empresa(saldo2)   
def pago_de_compra(cantidad):
    saldo = leer_saldo_cliente()
    if cantidad > saldo:
        print(f"No hay suficiente saldo. Saldo actual: {saldo:.2f}, intentaste gastar {cantidad:.2f}")
    else:
        saldo -= cantidad
        escribir_saldo_cliente(saldo)
        print(f"Se han gastado {cantidad:.2f} unidades. Saldo actual: {saldo:.2f}, Gracias por su compra.")
def añadir_saldo_pregunta():
    querer_añadir=str(input("¿Quieres depositar dinero? (si)(no)\n"))
    if querer_añadir.lower()=="si":
        añadir_dinero_cliente=float(input("Cuanto dinero vas a depositar:\n"))
        agregar_saldo_cliente(añadir_dinero_cliente)
    else:
        print("Okey, proseguiremos con la compra\n")


 
nombre_empresa=input("¿Como se llama tu empresa?\n")
print(f"Bienvenido, esta es la Empresa: {nombre_empresa}\n")

while repeticion == 0:

    añadir_saldo_pregunta()
    repeticion2=0
    while repeticion2==0:
        print(f"Esta es la lista de materiales que tenemos en nuestra empresa:\n {lista_materiales_grupos} \n")
        elegir_material=str(input("¿Que tipo de material quieres comprar (escribe solo el nombre del tipo no tienes que escribir el material)\n"))
        if elegir_material.lower()=="estructurales":
            print(materiales_estucturales)
            desicion_estructural=str(input("¿Cual de los materiales quieres?\n"))
            if desicion_estructural.lower()=="hormigon":
                cantidad_material_hormigon=float(input("¿Cuanta cantidad quiere?\n")) 
            repeticion2 += 1
        elif elegir_material.lower()=="acabado":
            print(materiales_estucturales)
            repeticion2 += 1
        elif elegir_material.lower()=="aislantes":
            print(materiales_estucturales)
            repeticion2 += 1
        elif elegir_material.lower()=="unionyadhesivos":
            print(materiales_estucturales)
            repeticion2 += 1
        elif elegir_material.lower()=="instalacione":
            print(materiales_estucturales)
            repeticion2 += 1
        elif elegir_material.lower()=="naturales":
            print(materiales_estucturales)
            repeticion2 += 1
        elif elegir_material.lower()=="recubrimiento":
            print(materiales_estucturales)
            repeticion2 += 1
        else:
            print("Elige un tipo de material que este en la lista / escribe adecuadamente el nombre del material")
            



    print(f"Esta es la cantidad a pagar:{cantidad_pago_total}\n")
    accion_pago=str(input("La desea pagar? (Si)(No):\n"))
    if accion_pago.lower() == "si":
        pago_de_compra(cantidad_pago_total)
    else:
        print("El pago ha sido cancelado")

    apagar_programa=str(input("Desea terminar el programa (Si)(No)\n"))
    if apagar_programa.lower() == "si":
        repeticion += 1
        print("Se finalizo el programa")
    else:
        print("")

