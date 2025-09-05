# reporte.py

def reporte_por_cantidad(ventas):
    return sorted(ventas.items(), key=lambda x: x[1]["cantidad"], reverse=True)

def reporte_por_ingreso(ventas):
    return sorted(ventas.items(), key=lambda x: x[1]["ingreso"], reverse=True)

def mostrar_reporte(ventas, orden="ingreso"):
    if orden == "cantidad":
        reporte = reporte_por_cantidad(ventas)
    else:
        reporte = reporte_por_ingreso(ventas)

    print("\n===== REPORTE DE VENTAS =====")
    for producto, datos in reporte:
        print(f"{producto}: Cantidad {datos['cantidad']} | Ingreso ${datos['ingreso']:.2f}")
