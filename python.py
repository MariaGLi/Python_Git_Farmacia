import json
import datetime
from os import system

with open("Compras.json", encoding="utf-8") as file:
    compra=json.load(file)

with open("Empleados.json", encoding="utf-8") as file2:
    empleados=json.load(file2)

with open("Medicamentos.json", encoding="utf-8") as file3:
    medicamento=json.load(file3)

with open("Pacientes.json", encoding="utf-8") as file4:
    pacientes=json.load(file4)

with open("Proveedores.json", encoding="utf-8") as file5:
    proveedor=json.load(file5)

with open("Ventas.json", encoding="utf-8") as file6:
    venta=json.load(file6)