""" #  El hotel Girasoles recolecta para sus estadísticas las reseñas de los clientes, por lo tanto
# antes de retirarse le solicita al huésped que deje su reseña del viaje. Devolviéndole el siguiente
# mensaje: ¡Gracias por la reseña detallada! ¡Esta tiene 20 caracteres! """

reseña = input("Ingrese reseña de del viaje: ")
reseña_new = reseña.replace(" ","").lower() # elimino espacios en blaco por el metodo replace()
print(f"¡Gracias por la reseña detallada! ¡Esta tiene {len(reseña_new)} caracteres!")

""" 
En la publicidad del hotel aparece ¡Los edificios 2, 7 y 9 son los más acogedores! Si elige este
hotel, entonces elija estos edificios. Obtener los números de los edificios para
Mostrar el mensaje Los clientes eligieron los edificios: 2 7 9 """

cadena = "¡Los edificios 2, 7 y 9 son los más acogedores! Si elige estehotel, entonces elija estos edificios."
# como es de la 15 a la 22 aproximadamente, python empieza en 0 las posiciones de memoria 
inicio = cadena.find("2") # recibe 3 parametros pero puede tomar uno en este caso el buscado

numeros= cadena[inicio:inicio+8]
print("Los clientes eligieron los hoteles: ",numeros.replace(","," ").replace("y","")) #muchos metodos permiten el aplicar uno tras otro en una sola linea

""" 
En el folleto del hotel figura ¡La vista al mar es una característica del hotel!
Muchos clientes han puesto en sus reseñas lo mucho que les ha gustado la visita al mar, se
pide mostrar la leyenda A nuestros clientes les gusta: La vista al mar. """

hotel = "¡La vista al mar es una característica del hotel!"

hotel = hotel.replace("¡","").replace("!","")

print(hotel.find("r")) # como es la "15"

nuevo_segmento = hotel[0:16] # voy de la posicion 1 la letra hasta el caracter

print(f"A nuestro clientes les gusta: {nuevo_segmento.lower()}")

"""  Para actualizar el menú del restaurante el chef necesita saber si quitar o dejar la torta de
chocolate y las brochetas. Por este motivo se le pide al cliente que Introduzca sus platos
favoritos del restaurante Girasol: .Se deberá mostrar si el postre esta o no dentro de los
favoritos para que el chef puede renovar el menú """

cliente_favs = input("Ingrese sus platillos favoritos: \n")

primer_plato = (cliente_favs.find("torta de chocolate"))
segundo_plato = cliente_favs.find("brocetas")

print("torta de chocolate: ", primer_plato)
print("brochetas:", segundo_plato)

# """ tambien puedo usar el metodo in cadena """

# print("torta de chocolate" in cliente_favs)
# print("brochetas" in cliente_favs)

""" 
Un hotel mágico con super restaurantes. Lo mejor en Chipre. Comida de alta calidad, una amplia variedad. Hermosa
playa y servicio. Habitaciones limpias y espaciosas! ¡Todo estuvo genial! La cocina japonesa deja una gran
impresión. Cuando vamos a Limassol, siempre pedimos sushi. Es muy difícil pasar por delante de un escaparate de
golosinas sin detenerse, aunque sólo sea para mirar. ¡Una zona tranquila!
El chef necesita saber si se ha mencionado los restaurantes y en especial el sushi. Mostrar cada uno con su
resultado de búsqueda dentro de la reseña.
"""
sushi = "Un hotel mágico con super restaurantes. Lo mejor en Chipre. Comida de alta calidad, una amplia variedad. Hermosa playa y servicio. Habitaciones limpias y espaciosas! ¡Todo estuvo genial! La cocina japonesa deja una granimpresión. Cuando vamos a Limassol, siempre pedimos sushi. Es muy difícil pasar por delante de un escaparate degolosinas sin detenerse, aunque sólo sea para mirar. ¡Una zona tranquila!"

restaurante = sushi.replace(","," ").replace("."," ").split()
""" coloco todo en minuscula, uso replace para  quitar las comas y puntos, y por ultimo split lo coloca en una lista asi cuento de  de forma mas sencilla las palabras"""
print("sushi" in restaurante, restaurante.count("sushi"),"shushi aparece en la posicion: ",sushi.find("sushi"))
print("Limassol" in restaurante, restaurante.count("restaurante"),"restaurante aparece en la posicion: ",sushi.find("restaurante"))

""" 
En Sunflowers, me gustó el personal atento.
El hotel quiere mostrar por pantalla la frase ‘’personal atento’’ para remarcar una
característica importante del hotel """

mensaje_final = "En Sunflowers, me gustó el personal atento, hola.".lower()
personal = mensaje_final.find("personal atento")
print(mensaje_final[personal:personal+len("personal atento")])
                                        # es un offset o desplazamiento le estoy diciendo que cuente despues de la letra p sumando la cantidad de caracteres que hay despues de la letra que busco, toma la posicion y empieza a contar de forma exacta
print(len("personal atento"))
#palabra[inicio:final]

""" 
personal: Es tu punto de partida (la letra "p").

len("personal atento"): Es la longitud de tu frase. Tiene exactamente 15 caracteres (contando el espacio).

Si le dices a Python que arranque en el número donde empieza la frase, y que termine en ese mismo número de inicio MÁS los 15 pasos que mide la frase, le estás dando exactamente el rango que necesita.
"""

print("-- Escriba una reseña de lo que no le gusto --")
reseña_cliente_buena = input("Describa aquello que le gusto: ")
reseña_cliente_mala = input("Describa aquello que no le gusto: ")
print("\n")
print(f"Gracias su descuento es de: {len(reseña_cliente_buena+reseña_cliente_buena)+len(reseña_cliente_buena+reseña_cliente_buena)*0.10:.2f} $ pesos")


reseña_entretenimiento = input("Buenas, ingrese porfavor alguna reseña de los juegos si lo desea :) ")
reseña_lista = reseña_entretenimiento.lower().split()

palabras_buscadas = ["divertido", "entretenido", "emocionante"]

conteo_final = [palabra for palabra in reseña_lista if palabra in palabras_buscadas]

cantidad = len(conteo_final)
print(len(conteo_final))

print(f"la cantidad de veces que aparecen las palabras es: {cantidad}")


# print([x for x in range(10) if x % 2])

# x = []
# for num in range(10):
#     if num % 2:
#         x.append(num)
        
# print(x)

# texto = input("diga algo: ").lower().split()
# palabras = ["hola"]
# contar = [x for x in texto if texto in palabras]
# print(contar)