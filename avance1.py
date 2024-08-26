import math 
import random
import os

lista_materiales_grupos="materiales estucturales, materiales acabado, materiales aislantes,\n materiales unionyadhesivos, materiales instalaciones, materiales naturales,\n materiales recubrimiento"
materiales_estucturales={"Hormigon":80,"Acero":1,"Madera":400,"Ladrillo":0.30,"Piedra":50,"Aluminio":2}
materiales_acabado={"Yeso":0.30,"Vidrio":20,"Tejas":0.50,"Pintura":10,"Baldosas":50,"Papel Pintado":4}
materiales_aislantes={"Lana Mineral":80,"Espuma de poliuretano":10,"Poliestireno expandido":5,"Corcho":15}
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
    print(f"Esta es la lista de materiales que tenemos en nuestra empresa:\n {lista_materiales_grupos} \n")
    while repeticion2==0:
        elegir_material=str(input("¿Que tipo de material quieres comprar (escribe solo el nombre del tipo no tienes que escribir el (material)\n"))
        print("\nsi quiere pagar escribe (Pagar)\n")

        if elegir_material.lower()=="estructurales":
            print(f"Los precios estan en pesos $:\n{materiales_estucturales}")

            repeticion3=0
            while repeticion3==0:
                desicion_estructural=str(input("Escoge el material (si quieres regresar escribe [r]):\n"))
                if desicion_estructural.lower()=="hormigon":
                    print(f"El valor del hormigon es de {materiales_estucturales['Hormigon']}$\n")
                    cantidad_material_hormigon=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_hormigon=cantidad_material_hormigon*materiales_estucturales["Hormigon"]
                    print(f"El precio del hormigon es de: {precio_hormigon}$\n")
                    cantidad_pago_total+=precio_hormigon
                    pregunta_terminar_hormigon=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_hormigon.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion3 += 1

                elif desicion_estructural.lower()=="acero":
                    print(f"El valor del acero es de {materiales_estucturales['Acero']}$/ metro cubico\n")
                    cantidad_material_acero=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_acero=cantidad_material_acero*materiales_estucturales["Acero"]
                    print(f"El precio del acero es de: {precio_acero}$\n")
                    cantidad_pago_total+=precio_acero
                    pregunta_terminar_acero=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_acero.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion3 += 1

                elif desicion_estructural.lower()=="madera":
                    print(f"El valor de la madera es de {materiales_estucturales['Madera']}$\n")
                    cantidad_material_madera=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_madera=cantidad_material_madera*materiales_estucturales["Madera"]
                    print(f"El precio de la madera es de {precio_madera}$\n")
                    cantidad_pago_total+=precio_madera
                    pregunta_terminar_madera=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_madera.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion3 += 1

                elif desicion_estructural.lower()=="ladrillo":
                    print(f"El valor del ladrillo es de {materiales_estucturales['Ladrillo']}$\n")
                    cantidad_material_ladrillo=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_ladrillo=cantidad_material_ladrillo*materiales_estucturales["Ladrillo"]
                    print(f"El precio del ladrillo es de: {precio_ladrillo}$\n")
                    cantidad_pago_total+=precio_ladrillo
                    pregunta_terminar_ladrillo=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_ladrillo.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion3 += 1
                
                elif desicion_estructural.lower()=="piedra":
                    print(f"El valor de la piedra es de {materiales_estucturales['Piedra']}$\n")
                    cantidad_material_piedra=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_piedra=cantidad_material_piedra*materiales_estucturales["Piedra"]
                    print(f"El precio de la piedra es de: {precio_piedra}$\n")
                    cantidad_pago_total+=precio_piedra
                    pregunta_terminar_piedra=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_piedra.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion3 += 1

                elif desicion_estructural.lower()=="aluminio":
                    print(f"El valor del aluminio es de {materiales_estucturales['Aluminio']}$\n")
                    cantidad_material_aluminio=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_aluminio=cantidad_material_aluminio*materiales_estucturales["Aluminio"]
                    print(f"El precio del aluminio es de: {precio_aluminio}$\n")
                    cantidad_pago_total+=precio_aluminio
                    pregunta_terminar_aluminio=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_aluminio.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion3 += 1
                
                elif desicion_estructural.lower()=="r":
                    repeticion3 += 1

                else:
                    print("elige un material de la lista/ escribe correctamente el material")
            
            
        elif elegir_material.lower()=="acabado":
            print(f"Los precios estan en pesos $:\n{materiales_acabado}")


            repeticion4=0
            while repeticion4==0:
                desicion_acabado=str(input("Escoge el material (si quieres regresar escribe [r]):\n"))
                if desicion_acabado.lower()=="yeso":
                    print(f"El valor del yeso es de {materiales_acabado['Yeso']}$\n")
                    cantidad_material_yeso=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_yeso=cantidad_material_yeso*materiales_acabado["Yeso"]
                    print(f"El precio del yeso es de: {precio_yeso}$\n")
                    cantidad_pago_total+=precio_yeso
                    pregunta_terminar_yeso=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_yeso.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion4 += 1

                elif desicion_acabado.lower()=="vidrio":
                    print(f"El valor del vidrio es de {materiales_acabado['Vidrio']}$/ metro cubico\n")
                    cantidad_material_vidrio=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_vidrio=cantidad_material_vidrio*materiales_acabado["Vidrio"]
                    print(f"El precio del vidrio es de: {precio_vidrio}$\n")
                    cantidad_pago_total+=precio_vidrio
                    pregunta_terminar_vidrio=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_vidrio.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion4 += 1

                elif desicion_acabado.lower()=="tejas":
                    print(f"El valor de las tejas es de {materiales_acabado['Tejas']}$\n")
                    cantidad_material_tejas=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_tejas=cantidad_material_tejas*materiales_acabado["Tejas"]
                    print(f"El precio de las tejas es de {precio_tejas}$\n")
                    cantidad_pago_total+=precio_tejas
                    pregunta_terminar_tejas=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_tejas.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion4 += 1

                elif desicion_acabado.lower()=="pintura":
                    print(f"El valor de la pintura es de {materiales_acabado['Pintura']}$\n")
                    cantidad_material_pintura=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_pintura=cantidad_material_pintura*materiales_acabado["Pintura"]
                    print(f"El precio del pintura es de: {precio_pintura}$\n")
                    cantidad_pago_total+=precio_pintura
                    pregunta_terminar_pintura=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_pintura.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion4 += 1
                
                elif desicion_acabado.lower()=="baldosas":
                    print(f"El valor de las baldosas es de {materiales_acabado['Baldosas']}$\n")
                    cantidad_material_baldosas=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_baldosas=cantidad_material_baldosas*materiales_acabado["Baldosas"]
                    print(f"El precio de las baldosas es de: {precio_baldosas}$\n")
                    cantidad_pago_total+=precio_baldosas
                    pregunta_terminar_baldosas=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_baldosas.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion4 += 1

                elif desicion_acabado.lower().replace(" ","")=="papelpintado":
                    print(f"El valor del papel pintado es de {materiales_acabado['Papel Pintado']}$\n")
                    cantidad_material_papel_pintado=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_papel_pintado=cantidad_material_papel_pintado*materiales_acabado["Papel Pintado"]
                    print(f"El precio del papel pintado es de: {precio_papel_pintado}$\n")
                    cantidad_pago_total+=precio_papel_pintado
                    pregunta_terminar_papel_pintado=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_papel_pintado.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion4 += 1
                
                elif desicion_acabado.lower()=="r":
                    repeticion4 += 1

                else:
                    print("elige un material de la lista/ escribe correctamente el material")



            
        elif elegir_material.lower()=="aislantes":
            print(f"Los precios estan en pesos $:\n{materiales_aislantes}")


            repeticion5=0
            while repeticion5==0:
                desicion_aislantes=str(input("Escoge el material (si quieres regresar escribe [r]):\n"))

                if desicion_aislantes.lower().replace(" ", "")=="lanamineral":
                    print(f"El valor de la lana mineral es de {materiales_aislantes['Lana Mineral']}$\n")
                    cantidad_material_lana_mineral=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_lana_mineral=cantidad_material_lana_mineral*materiales_aislantes["Lana Mineral"]
                    print(f"El precio de la lana mineral es de: {precio_lana_mineral}$\n")
                    cantidad_pago_total+=precio_lana_mineral
                    pregunta_terminar_lana_mineral=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_lana_mineral.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion5 += 1

                elif desicion_aislantes.lower().replace(" ","")=="espumadepoliuretano":
                    print(f"El valor de la Espuma de poliuretano es de {materiales_aislantes['Espuma de poliuretano']}$/ metro cubico\n")
                    cantidad_material_espuma=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_espuma=cantidad_material_espuma*materiales_aislantes["Espuma de poliuretano"]
                    print(f"El precio de la Espuma de poliuretano es de: {precio_espuma}$\n")
                    cantidad_pago_total+=precio_espuma
                    pregunta_terminar_espuma=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_espuma.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion5 += 1

                elif desicion_aislantes.lower().replace(" ","")=="poliestirenoexpandido":
                    print(f"El valor del Poliestireno expandido es de {materiales_aislantes['Poliestireno expandido']}$\n")
                    cantidad_material_expandido=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_expandido=cantidad_material_expandido*materiales_aislantes["Poliestireno expandido"]
                    print(f"El precio del Poliestireno expandido es de {precio_expandido}$\n")
                    cantidad_pago_total+=precio_expandido
                    pregunta_terminar_expandido=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_expandido.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion5 += 1

                elif desicion_aislantes.lower()=="corcho":
                    print(f"El valor del corcho es de {materiales_aislantes['Corcho']}$\n")
                    cantidad_material_corcho=float(input("¿Cuanta cantidad quiere?\n"))
                    precio_corcho=cantidad_material_corcho*materiales_aislantes["Corcho"]
                    print(f"El precio del corcho es de: {precio_corcho}$\n")
                    cantidad_pago_total+=precio_corcho
                    pregunta_terminar_corcho=str(input("¿Quieres elegir otro material? (si)(no):\n "))
                    if pregunta_terminar_corcho.lower()=="si":
                        print("-------------------")
                    else:
                        repeticion5 += 1
                
                elif desicion_acabado.lower()=="r":
                    repeticion5  += 1

                else:
                    print("elige un material de la lista/ escribe correctamente el material")


        elif elegir_material.lower() and elegir_material.strip()=="unionyadhesivos":
            print(materiales_unionyadhesivos)
            repeticion2 += 1
        elif elegir_material.lower()=="instalaciones":
            print(materiales_instalaciones)
            repeticion2 += 1
        elif elegir_material.lower()=="naturales":
            print(materiales_naturales)
            repeticion2 += 1
        elif elegir_material.lower()=="recubrimiento":
            print(materiales_recubrimiento)
            repeticion2 += 1
        elif elegir_material.lower()=="pagar":
            repeticion2 += 1
        else:
            print("Elige un tipo de material que este en la lista / escribe adecuadamente el nombre del material")
            



    print(f"Esta es la cantidad a pagar:{cantidad_pago_total}\n")
    accion_pago=str(input("La desea pagar? (Si)(No):\n"))
    if accion_pago.lower() == "si":
        pago_de_compra(cantidad_pago_total)
    else:
        print("El pago ha sido cancelado")
        cantidad_pago_total==0

    apagar_programa=str(input("Desea terminar el programa (Si)(No)\n"))
    if apagar_programa.lower() == "si":
        repeticion += 1
        print("Se finalizo el programa")
    else:
        print("")

