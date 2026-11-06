"""
Archivo: ejercicio4_expedicion.py
Curso: SOFT-01 Principios de Programación 1
Autor: Edgar Luis Alfaro Quirós
Fecha: 2026-11-06
Versión: 1.0
Descripción: Simula el consumo diario de agua y alimento de una expedición y
determina si puede completar su duración programada.
"""

AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100
JORNADAS_MINIMAS = 1
JORNADAS_MAXIMAS = 30

# Entrada con validación de la cantidad de jornadas
jornadas_planeadas = int(input("Cantidad de jornadas (1 a 30): "))
while jornadas_planeadas < JORNADAS_MINIMAS or jornadas_planeadas > JORNADAS_MAXIMAS:
    print("Error: ingrese un número entero entre 1 y 30.")
    jornadas_planeadas = int(input("Cantidad de jornadas (1 a 30): "))

# Inicialización
agua_restante = AGUA_INICIAL
alimento_restante = ALIMENTO_INICIAL
agua_consumida = 0
alimento_consumido = 0
dias_completados = 0
estado = "Completada"

# Iteración sobre las jornadas planeadas
for dia in range(1, jornadas_planeadas + 1):
    print(f"\n--- Jornada {dia} ---")
    print(f"Disponible: {agua_restante} L de agua, {alimento_restante} unidades de alimento")

    # Validación del consumo de agua
    agua_dia = float(input("Agua consumida (litros): "))
    while agua_dia <= 0 or agua_dia > agua_restante:
        print(f"Error: el consumo debe ser mayor que 0 y no superar {agua_restante} litros.")
        agua_dia = float(input("Agua consumida (litros): "))

    # Validación del consumo de alimento
    alimento_dia = float(input("Alimento consumido (unidades): "))
    while alimento_dia <= 0 or alimento_dia > alimento_restante:
        print(f"Error: el consumo debe ser mayor que 0 y no superar {alimento_restante} unidades.")
        alimento_dia = float(input("Alimento consumido (unidades): "))

    # Proceso: actualización de existencias y acumuladores
    agua_restante = agua_restante - agua_dia
    alimento_restante = alimento_restante - alimento_dia
    agua_consumida = agua_consumida + agua_dia
    alimento_consumido = alimento_consumido + alimento_dia
    dias_completados = dias_completados + 1

    print(f"Saldo: {agua_restante} L de agua, {alimento_restante} unidades de alimento")

    # Interrupción anticipada si algún recurso se agotó y quedan jornadas
    if (agua_restante == 0 or alimento_restante == 0) and dia < jornadas_planeadas:
        estado = "Interrumpida por agotamiento de recursos"
        print("Un recurso se agotó. La expedición no puede continuar.")
        break

# Salida: informe final
promedio_agua = agua_consumida / dias_completados
promedio_alimento = alimento_consumido / dias_completados

print("\n===== INFORME FINAL =====")
print(f"Días completados: {dias_completados} de {jornadas_planeadas}")
print(f"Agua consumida: {agua_consumida} L")
print(f"Alimento consumido: {alimento_consumido} unidades")
print(f"Agua restante: {agua_restante} L")
print(f"Alimento restante: {alimento_restante} unidades")
print(f"Promedio diario de agua: {promedio_agua:.2f} L")
print(f"Promedio diario de alimento: {promedio_alimento:.2f} unidades")
print(f"Estado de la expedición: {estado}")
