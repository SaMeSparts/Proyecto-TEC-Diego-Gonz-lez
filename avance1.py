import math 
import random


nombre_empresa=input("¿Como se llama tu empresa?")
dinero_cliente=0
dinero_empresa=0

print(f"Bienvenido, esta es la Empresa: {nombre_empresa}")

materiales_estucturales={"Hormigon":80,"Acero":1,"Madera":400,"Ladrillo":0.30,"Piedra":50,"Aluminio":2}
materiales_acabado={"Yeso":0.30,"Vidrio":20,"Tejas":0.50,"Pintura":10,"Baldosas":50,"Papel Pintado":4}
materiales_aislantes={"Lana Mineral":80,"Espuma de poliuretano":10,"Poliestireno expandido":5,"Corcho:":15}
materiales_unionyadhesivos={"Cemento":8,"Mortero":5,"Siliconas":4,"Resinas epoxi":20}
materiales_instalaciones={"Cobre":8,"PVC":1,"Polipropileno":4,"Acero galvanizado":3,}
materiales_naturales={"Madera":400,"Bambú":1,"Adobe":0.10,"Piedra":50}
materiales_recubrimiento={"Enyesado":6,"Pladur":10,"Azulejos":25,"Mármol":100}

print(materiales_acabado)
