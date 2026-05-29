""" comunidad IT """

print("hola mundo")

def salarios(sueldo, meses):
    return f"Importe total del salario de los empleados {sueldo * meses:,.2f} $ pesos"

print(salarios(53670, 12))

def nuevo_precio(alquiler, aumento):
    return f"Aumento para el proximo mes de: {alquiler + alquiler * aumento:,.2f} $ pesos"

print(nuevo_precio(85000,0.10))

def cuenta(cantidad,dias):
    return f"Se venden por dia: {cantidad/dias:,.2f} paquetes de yerba"
print(cuenta(2920,365))