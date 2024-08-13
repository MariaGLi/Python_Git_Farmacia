import json
import datetime
from os import system

with open("Jsons/Compras.json", encoding="utf-8") as file:
    compra=json.load(file)

with open("Jsons/Empleados.json", encoding="utf-8") as file2:
    empleados=json.load(file2)

with open("Jsons/Medicamentos.json", encoding="utf-8") as file3:
    medicamento=json.load(file3)

with open("Jsons/Pacientes.json", encoding="utf-8") as file4:
    pacientes=json.load(file4)

with open("Jsons/Proveedores.json", encoding="utf-8") as file5:
    proveedor=json.load(file5)

with open("Jsons/Ventas.json", encoding="utf-8") as file6:
    venta=json.load(file6)

sel=0
while sel!=4:
    system("cls")
    print("------------------- BIENVENIDO AL MENÚ -------------------\n")
    print("""
    1. Venta
    2. Compra
    3. Generación de informes
    4. Salir
    """)
    inicio=int(input("Digita el numero de lo primero que deseas hacer:\n"))

    if inicio==1:
        compemp=str(input("Digite el nombre del empleado:\n"))
        compemp=0
        for i in empleados:
            cont=+1
            if compemp == i["nombre"]:
                Cont=0
                for g in medicamento:
                    Cont+=1
                    print(Cont,".", g["nombre"])

                comp=str(input("Ingrese el nombre del producto a vender: \n"))
                for m in medicamento:
                    if comp == m["nombre"]:
                        print("El producto que has elegido es: ", m)
                        cant=int(input("Ingrese la cantidad a vender:\n"))
                        Npaciente=str(input("Ingrese el nombre del paciente:\n"))
                        direcpaciente=(input("Ingrese la dirección del pcte:\n"))
                        total=cant*m["precio"]
                        fecha=str(datetime.datetime.now())