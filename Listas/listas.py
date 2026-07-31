""" 
    2- Dada la siguiente lista de usuarios : 'max123', 'sweet_girl', 'funJohn', 'crazy.cat‘.
Se solicita mostrarla numerada ascendentemente y en orden Alfabético, con el título de Listado de usuarios.
Al finalizar, además se deberá indicar Usuarios totales y su cantidad.
"""
lista = ['max123', 'sweet_girl', 'funJohn', 'crazy.cat']
lista.sort()
print("Listado de usuarios: ")
print(lista)
print("cantidad total de usuarios: ",len(lista))


"""
3- Una tienda de videojuegos desea realizar un programa que en base a la solicitud de un videojuego por
Parte del usuario le responda Contamos con ese videojuego o No lo tenemos por el momento.
La tienda tiene los siguientes videojuegos disponibles: 'dota 2', 'cs go', 'warface', 'minecraft' .
"""
lista_juegos = ['dota 2', 'cs go', 'warface', 'minecraft']
peticion_usuario = input("Ingrese el juego que quiere comprar: ")
if peticion_usuario not in lista_juegos:
    print("perdone el juego que busca no lo tenemos")
else:
    print("el juego que busca se encuentra: ")



"""
4- Para hacer un relevamiento de los juegos que deberá incorporar la tienda a su catálogo, solicita un programa
Para recolectar las preferencias de sus usuarios, para ello le interesa armar por usuario una lista de sus juegos Preferidos. El programa debe pedirle al usuario que Introduzca el juego (0 - detener la entrada):
En el caso de que introduzca repetidos se le deberá informar que ese juego ya fue registrado.
Al finalizar se deberá mostrar la lista ordenada de juegos del usuario.
"""
juegos = []
while True:
    ingreso = input("ingrese sus juegos favoritos o escriba salir para terminar >>: ")
    if ingreso.lower() == 'salir':
        break
    else:
        if ingreso in juegos:
            print("Ese juego ya gue ingresado previamente")
    juegos.append(ingreso)
print("-----")
#con sort()
juegos.sort()
print(*juegos, end= '')
print("\n-----")
# formato desempaquetado con el operador *sorted([lista])
print(*sorted(juegos))
# otra forma es usando un for que recorra la lista y sorted que es el metodo de listas usando tim sort
print("\n-----")
for i in sorted(juegos):
    print(i, end=' ')

print("\n-----")
"""
5- El curso de una escuela empezó con los siguientes estudiantes :
'Abrams', 'Khanna', 'Lee', 'Freeland', 'Qadiri‘. Para principios de agosto se sumarán otros estudiantes. Para que
Se mantenga actualizada la lista del curso, la escuela requiere un programa que cumpla con esa tarea. Cada
Vez que se agregan estudiantes la escuela necesita conocer el listado enumerado y ordenado alfabéticamente
Anterior y posterior a los ingresos. Ejemplo de salida
Listado de alumnos
1-Abrams
2-Khanna
.
.
6- Para la evaluación final de contenidos de una materia el profesor decidió realizar tantos temas como estudiantes haya en
el aula. Es decir, si se anotaron 5 estudiantes se realizan 5 pruebas numeradas de 1 a 5 y se asignara a cada alumno un
número correspondiente a una prueba de forma aleatoria.
Para desarrollar el programa se solicitara que se Introduzca los nombres de los estudiantes separados por un espacio (todos
al mismo tiempo). Al finalizar se mostrará
Distribución de las variantes de la prueba
Juan - 2
Pedro – 3
Luisa -5
7- Para conocer el porcentaje de los 10 que se saca un alumno en Matemática durante el año, se le solicita que
Introduzca las notas separadas por un espacio: y que una vez que se procesen las notas le indique
Calificaciones 10 recibidas (%) – porcentaje
8- Se desea crear una lista con edades de personas entrevistadas para una encuesta mientras el usuario lo requiera, no se
permiten edades menores que 13 años ni mayores que 120
- hallar la edad mínima (sin usar min)
- calcular el promedio de edades
- contar cuántas personas mayores a 60 hay (sin usar count)
- reemplazar todas las edades menores a 18 con las palabras “menor de edad”
- El programa además debe listar las edades una debajo de la otra de la siguiente manera:
Persona 1: 19
Persona 2: 22
Persona 3: menor de edad
Persona 4: 67 y así sucesivamente
9-Crear una lista con los nombres de todos los estudiantes para rendir el examen, indicando “fin” para terminar la carga.
-A cada estudiante se le asigna un número aleatorio para su turno de rendir la prueba (hay tantas variantes como el
número de estudiantes y se pueden repetir).
-Mostrar las asignaciones de los turnos con el título “Distribución de los turnos de la prueba”
Se mostrará una lista de los nombres con los números de variante asignados de la siguiente manera:
Luis – 2
María -1
Ernesto – 3
Carlos – 2 y así tantos estudiantes se hayan cargado
-Según el número obtenido se deberá reemplazar por la leyenda “rinde hoy” si el número es par o “rinde mañana” si es
impar.
-Mostrar la cantidad de alumnos en cada turno. Con la leyenda “Cantidad de alumnos que rinden hoy” y “Cantidad de
alumnos que rinden mañana” con los respectivos totales.

"""