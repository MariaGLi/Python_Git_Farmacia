import json
from os import system

with open("Pacientes.json", encoding="utf-8") as file4:
    pacientes=json.load(file4)

with open("Proveedores.json", encoding="utf-8") as file5:
    proveedor=json.load(file5)

with open("Ventas.json", encoding="utf-8") as file6:
    venta=json.load(file6)