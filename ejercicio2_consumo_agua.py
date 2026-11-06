"""
Archivo: ejercicio2_consumo_agua.py
Curso: SOFT-01 Principios de Programación 1
Autor: Edgar Luis Alfaro Quirós
Fecha: 2026-11-06
Versión: 1.0
Descripción: Registra el consumo diario de agua durante siete días y calcula
total, promedio, consumo máximo y días que superan el umbral de referencia.
"""

DIAS_SEMANA = 7
UMBRAL_LITROS = 150

# Inicialización de acumuladores y contadores
consumo_total = 0
consumo_maximo = 0
dias_sobre_umbral = 0

# Iteración: la cantidad de días es conocida, se usa for
for dia in range(1, DIAS_SEMANA + 1):
    # Entrada con validación (valores >= 0)
    consumo_dia = float(input(f"Consumo del día {dia} (litros): "))
    while consumo_dia < 0:
        print("Error: el consumo debe ser mayor o igual a cero.")
        consumo_dia = float(input(f"Consumo del día {dia} (litros): "))

    # Proceso
    consumo_total = consumo_total + consumo_dia
    if consumo_dia > consumo_maximo:
        consumo_maximo = consumo_dia
    if consumo_dia > UMBRAL_LITROS:
        dias_sobre_umbral = dias_sobre_umbral + 1

promedio_diario = consumo_total / DIAS_SEMANA

# Salida
print("----- Resumen semanal -----")
print(f"Consumo total: {consumo_total:.2f} litros")
print(f"Promedio diario: {promedio_diario:.2f} litros")
print(f"Mayor consumo: {consumo_maximo:.2f} litros")
print(f"Días que superaron {UMBRAL_LITROS} litros: {dias_sobre_umbral}")
