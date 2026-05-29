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

""" ejercicios con variables """

# guia = str(input("ingrese al guia: "))
alumnos = 24
nombre_guia = "Juan Perez"
valor_persona = 2450

print(f"Guia: {nombre_guia} \nPrecio total del paquete: {alumnos * valor_persona:,.2f} $")

adulto = 3700 
menor = 1100
cantidad_adulto = 2
cantidad_menor = 31
print(f"precio total a pagar: {cantidad_adulto*adulto+31*cantidad_menor:,.2f}$ pesos")

equipaje = 2000
pasaportes = 1100
transporte = 4500

print(f"Precio total del seguro: {(equipaje + pasaportes + transporte)*3:,.2f} $")

precio_mayo = 100000
aumento_agosto = .35
aumento_noviembre = .25

print(f"Precio de mayo: {precio_mayo:,.2f}$\nAgosto: {precio_mayo + precio_mayo * aumento_agosto:,.2f}$\nNoviembre: {precio_mayo + (precio_mayo * aumento_agosto) *(1+aumento_noviembre):,.2f}$")

add = int(input("coloca numero"))
total = 255 + int(add)
print(total)

texto = str(input("esto sera texto"))
texto1 = "hola "+ texto
print(texto1)

