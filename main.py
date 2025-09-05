from registro import RegistroVentas
from calculos import calcular_ingreso_total
from reporte import mostrar_reporte

def main():
    registro = RegistroVentas()

    print("=== SISTEMA DE CONTROL DE VENTAS ===")
    while True:
        producto = input("Ingrese nombre del producto (o 'salir' para terminar): ")
        if producto.lower() == "salir":
            break
        try:
            cantidad = int(input("Ingrese cantidad vendida: "))
            precio = float(input("Ingrese precio unitario: "))
            registro.agregar_venta(producto, cantidad, precio)
        except ValueError:
            print(" Error: ingrese números válidos para cantidad y precio.")

    # Mostrar resultados
    total = calcular_ingreso_total(registro.ventas)
    print(f"\n Ingreso total del día: ${total:.2f}")

    # Elegir cómo mostrar reporte
    opcion = input("¿Desea ver reporte ordenado por (ingreso/cantidad)? ").lower()
    mostrar_reporte(registro.ventas, orden=opcion)

if __name__ == "__main__":
    main()