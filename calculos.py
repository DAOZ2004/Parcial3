# calculos.py

def calcular_ingreso_total(ventas):
    return sum(datos["ingreso"] for datos in ventas.values())

def calcular_mas_vendido(ventas):
    return max(ventas.items(), key=lambda x: x[1]["cantidad"])

def calcular_mayor_ingreso(ventas):
    return max(ventas.items(), key=lambda x: x[1]["ingreso"])
