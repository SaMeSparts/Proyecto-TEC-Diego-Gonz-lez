import os

saldo_cliente="saldocliente.txt"
saldo_empresa="saldoempresa.txt"


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
    print(f"Se han agregado {cantidad:.2f} unidades. Saldo actual: {saldo:.2f}")
def agregar_saldo_empresa(cantidad2):
    saldo2 = leer_saldo_empresa()
    saldo2 += cantidad2
    escribir_saldo_empresa(saldo2)
    print(f"Se han agregado {cantidad2:.2f} unidades. Saldo actual: {saldo2:.2f}")

añadir_dinero_cliente=float(input("Cuanto dinero vas a depositar:\n"))
agregar_saldo_cliente(añadir_dinero_cliente)
