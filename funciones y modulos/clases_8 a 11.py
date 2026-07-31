""" 
6- Un crucero ofrece a sus pasajeros la posibilidad de agregar servicios a su estadía. El precio del boleto es

De $70000, a este valor el pasajero puede sumarle si desea un seguro a bordo por $30000 , y/o bebidas con

alcohol por $50000. Luego de las decisiones del pasajero se le deberá informar

El precio de su boleto incluyendo los servicios elegidos:

7- Una escuela desea felicitar a los estudiantes recibidos con promedio de 10, para ello se deberá crear un programa que

Solicite la cantidad de estudiantes con ese promedio y por cada estudiante se consultará el nombre y apellido

Para mostrar la siguiente leyenda:

Nos gustaría expresar nuestra gratitud hacia nombre y apellido

La institución lo felicita por el final de este curso escolar y les desea futuros éxitos en los estudios.

8-Escriba un programa que evalúe el progreso del estudiante durante sus prácticas

Cada alumno podría elegir cualquier cantidad de materias a estudiar. En cada materia, pueden obtener desde 0 hasta 50

puntos. El programa debe:

1. Solicitar el nombre del estudiante y el número de materias.

2. Solicitar el puntaje para cada materia e imprimir la cantidad total de puntos: "Puntaje final: _".

3. Según la suma de los puntos, determinar el tipo de certificado de prácticas:

– más de 80 puntos — "Conceder un diploma.";

– el número de puntos es mayor que 50 y menor o igual que 80 — "Conceder un certificado de apreciación.";

– en cualquier otro caso – "Conceder un certificado de participación.

" El conteo de puntos y la asignación de diplomas se definen como funciones.

9-Escribir el código de las funciones invocadas en este main()

Además, completen los espacios en blanco correspondientes al main()

El programa debe calcular cuántas ventas de cada electrodoméstico hubo y el monto promedio de las ventas

………………………………………………………………………………

………………………………………………………………………………

………………………………………………………………………………

while seguir == "si":

electrodomestico = Preguntar_electrodomestico() #se debe ingresar celular, tv u otro sino lo vuelve a pedir

precio = Ingresar_precio() #debe ser positivo

if electrodoméstico == "celular":

………………………………………………………………………………………

………………………………………………………………………………

………………………………………………………………………………………

seguir = Preguntar_si_se_desea_continuar() #se debe ingresar si o no

promedio = Hallar_Promedio(sumaprecios,cantidad)

Informar_Resultado("celular",contcel)

Informar_Resultado("tv",contv)

Informar_Resultado("otros",contotros)

print("Venta Promedio: " , promedio)
"""


""" 
6- Un crucero ofrece a sus pasajeros la posibilidad de agregar servicios a su estadía. El precio del boleto es
De $70000, a este valor el pasajero puede sumarle si desea un seguro a bordo por $30000 , y/o bebidas con
alcohol por $50000. Luego de las decisiones del pasajero se le deberá informar
El precio de su boleto incluyendo los servicios elegidos:
"""

# ejercicio 6

def eje6(precio_base):
    total = 0
    
    seguro = input("Desea agregar un seguro a bordo del barco? si/no: ").lower()
    bebida = input("Desea agregar bebidas con alcohol? si/no: ").lower()
    
    total = precio_base
    if seguro == 'si':
        total += 30000
    if bebida == 'si':
        total += 50000
    
    return f"el precio por su eleccion es de ${total}"

print(eje6(70000))

""" 
7- Una escuela desea felicitar a los estudiantes recibidos con promedio de 10, para ello se deberá crear un programa que
Solicite la cantidad de estudiantes con ese promedio y por cada estudiante se consultará el nombre y apellido
Para mostrar la siguiente leyenda:
Nos gustaría expresar nuestra gratitud hacia nombre y apellido
La institución lo felicita por el final de este curso escolar y les desea futuros éxitos en los estudios.
"""
def cant_estudiante(cantidad):
    for i in range(cantidad):
        nombre_apellido = input(f"Ingrese el nombre y apellido del estudiante {i+1}")
        print(f"Nos gustaria expresar nuestra gratitud hacia {nombre_apellido}")
        print("La institución lo felicita por el final de este curso escolar y les desea futuros éxitos en los estudios")
# print(cant_estudiante(input(int("ingrese la cantidad de estudiantes: "))))

cantidad_str = input("Ingrese la cantidad de estudiantes: ")
cantidad = int(cantidad_str)
print(cant_estudiante(cantidad))
# otro seria un bucle que recorra una lista de nombres y apellidos asi la cosa sale mas sensata en vez de uno por uno
# tambien mas sencillo todavia un diccionario pero boeeee se complican mucho se ve

lista = []
cantidad = 3
for i in range(cantidad):
    nombre = input(f"ingrese nombre y apellido {i + 1} ")
    lista.append(nombre)
