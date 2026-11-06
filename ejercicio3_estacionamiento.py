"""
Archivo: ejercicio3_estacionamiento.py
Curso: SOFT-01 Principios de Programación 1
Autor: Edgar Luis Alfaro Quirós
Fecha: 2026-11-06
Versión: 1.0
Descripción: Sistema de consola para administrar un estacionamiento privado
de 20 espacios con cobro de ₡800 por hora.
"""

CAPACIDAD = 20
TARIFA_HORA = 800

# Inicialización
ocupacion = 0
salidas = 0
recaudacion = 0

# Iteración: el menú se repite hasta seleccionar la opción 5
while True:
    print("\n===== ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    # Decisión múltiple
    if opcion == "1":
        if ocupacion < CAPACIDAD:
            ocupacion = ocupacion + 1
            print(f"Ingreso registrado. Ocupación: {ocupacion}/{CAPACIDAD}")
        else:
            print("No hay espacios disponibles.")
    elif opcion == "2":
        if ocupacion > 0:
            horas = int(input("Horas por cobrar: "))
            while horas <= 0:
                print("Error: las horas deben ser un entero mayor que cero.")
                horas = int(input("Horas por cobrar: "))
            pago = horas * TARIFA_HORA
            ocupacion = ocupacion - 1
            salidas = salidas + 1
            recaudacion = recaudacion + pago
            print(f"Salida registrada. Monto a pagar: ₡{pago}")
        else:
            print("No hay vehículos en el estacionamiento.")
    elif opcion == "3":
        print(f"Espacios ocupados: {ocupacion}")
        print(f"Espacios libres: {CAPACIDAD - ocupacion}")
    elif opcion == "4":
        print(f"Recaudación total: ₡{recaudacion}")
        print(f"Vehículos que han salido: {salidas}")
    elif opcion == "5":
        print("\n----- Resumen final -----")
        print(f"Vehículos presentes: {ocupacion}")
        print(f"Salidas procesadas: {salidas}")
        print(f"Recaudación total: ₡{recaudacion}")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
