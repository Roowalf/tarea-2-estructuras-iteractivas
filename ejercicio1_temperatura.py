"""
Archivo: ejercicio1_temperatura.py
Curso: SOFT-01 Principios de Programación 1
Autor: Edgar Luis Alfaro Quirós
Fecha: 2026-11-06
Versión: 1.0
Descripción: Simula el calentamiento de una cámara experimental con un
incremento fijo por ciclo hasta alcanzar o superar la temperatura objetivo.
"""

# Entrada
temperatura_inicial = float(input("Temperatura inicial (°C): "))
temperatura_objetivo = float(input("Temperatura objetivo (°C): "))
incremento = float(input("Incremento por ciclo (°C): "))

# Decisiones: validación de la configuración
configuracion_valida = True

if temperatura_objetivo <= temperatura_inicial:
    print("Error: la temperatura objetivo debe ser mayor que la temperatura inicial.")
    configuracion_valida = False

if incremento <= 0:
    print("Error: el incremento debe ser estrictamente positivo.")
    configuracion_valida = False

if configuracion_valida:
    # Inicialización de las variables del ciclo
    temperatura_actual = temperatura_inicial
    ciclos = 0

    # Iteración: continúa mientras no se alcance el objetivo
    while temperatura_actual < temperatura_objetivo:
        temperatura_actual = temperatura_actual + incremento  # actualización
        ciclos = ciclos + 1
        print(f"Ciclo {ciclos}: {temperatura_actual} °C")

    # Salida
    print(f"Temperatura alcanzada: {temperatura_actual} °C")
    print(f"Total de ciclos: {ciclos}")
else:
    print("La simulación no se ejecutó.")
