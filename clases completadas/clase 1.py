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

""" 
    Desde la Web de la agencia de turismo podemos calcular el precio total del costo de los pasajes de avión.
    Para eso debemos indicarle al usuario que:
    Introduzca el precio para un boleto:
    Introduzca la cantidad de turistas:
    Mostrar
    Precio total 
"""
precio_boleto = float(input("Introduzca el precio de un boleto: \n"))
cant_turistas = int(input("Introduzca cantidad de turistas: \n"))

print(f"Precio total: {precio_boleto * cant_turistas:,.2f} $")

nombre_cliente = input("Nombre del Cliente: \n")
cant_viajes = int(input("Cantidad de paquetes comprados: \n")) 
destinos_fav = input("Destinos preferidos: \n")

""" 
    Para armar un presupuesto la agencia necesita los siguientes datos:
    Introduzca el apellido:
    Introduzca el país de destino:
    Introduzca la temporada:
    La página Web responderá : Solicitud – Pedro Francia Otoño – enviado
"""
apellido = input("Ingrese apellido: \n")
destino = input("Introduzca el destino: \n")
temporada = input("Ingrese temporada: \n")

print("Solicitud –",apellido, destino, temporada," – enviado")

""" 
    Para calcular el hospedaje se necesitan conocer los siguientes datos:
    Introduzca el precio de una noche en el hotel:
    Introduzca el número de días de descanso:
    Se mostrará: 
    Precio del paquete:
"""
precio = int(input("Intrduzca el precio de una noche en el hotel: \n"))
dias = int(input("Introduzca el número de días de descanso: \n"))

print(f"Precio del paquete: {precio * dias:,.2f}$ pesos")

# Durante este mes la agencia cuenta con 20% de descuento con pago en efectivo y 15% con tarjeta. Para
# conocer el monto a pagar se deberá solicitar al cliente.
# Introduzca el precio del boleto:
# Introduzca el medio de pago o monto de la bonificación:
# Se mostrará: Precio con descuento:

precio_bol = int(input("Ingrese el precio del boleto: \n"))
medio_pago = input("Ingrese el medio de pago: efectivo/ tarjeta: \n")
total = 0

if medio_pago.lower() == 'efectivo':
    total = total + (precio_bol + (precio_bol * 0.20))
    print(f"Precio condescuento: {total}")
else:
    if medio_pago.lower() == 'tarjeta':
        total = total + (precio_bol + (precio_bol * 0.15))
        print(f"Precio condescuento: {total}")


print (f"Hola {nombre_cliente}\nUsted ya viajo con nosotros {cant_viajes} vez/veces ¿Le gustaria volver a viajar?\nNuestra agencia de viajes esta dando una oferta. ¡Viaje a {destinos_fav} con 50% de descuento!")

cliente = input("Nombre del Cliente: \n")
fecha_nac = input("Fecha de nacimiento en formato dd/mm/aaaa: \n")
celular = int(input("Ingrese numero de telefono: \n")) 

print(f"El cliente {cliente} se añadio a la base de datos")

"""  """