""" 
    1- En la pastelería están ofreciendo productos dulces de oferta, Para recomendar el producto correcto le
    consulta a sus clientes si quieren conocer las ofertas y de qué categoría (dulce, salado). Si el cliente
    quiere recibir ofertas de dulces. La panadería muestra el mensaje Torta de frambuesa por solo $3500. Si
    quiere recibir ofertas pero de salado se le recomienda Tarta de queso por $4500. Si no le interesan las
    ofertas se le informa Si cambia de opinión , consulte nuevamente
"""
continua = input("Quiere consultar? si/no: ")
while continua == 'si':
    opcion = input("Desea conocer las ofertas? si/no: ").lower()

    if opcion == 'si':
        opcion_cli = int(input("seleccione la categoria que quiere conocer dulce o salado: 1. Dulce o 2.Salados\t"))
        if opcion_cli == 1:
            print("Podemos ofrecerle; Torta de frambuesa por $3500")
        elif opcion_cli == 2:
            print("Podemos ofrecerle; Torta de queso por $4500\n")
        
        continua = input("¿Desea realizar otra consulta? (si/no): ").lower()
    else:
        print("Si cambia de opinion puede consultar nuevamente, que tenga buen dia")
        continua = 'no'
        


while True:
    opcion = input("Desea conocer las ofertas? si/no: ").lower()

    if opcion == 'si':
        opcion_cli = int(input("seleccione la categoria que quiere conocer dulce o salado: 1. Dulce o 2.Salados\t"))
        
        if opcion_cli == 1:
            print("Podemos ofrecerle; Torta de frambuesa por $3500")
        elif opcion_cli == 2:
            print("Podemos ofrecerle; Torta de queso por $4500\n")
        else:
            print("Opcion no valida")
            
    elif opcion == 'no':
        print("Si cambia de opinion puede consultar nuevamente, que tenga buen dia")
        break
    else:
        print("Solo ingrese si o no")
        
        
""" 
    2- Una huerta orgánica está instalada en el barrio, para darse a conocer arma para sus clientes combos
    de frutas, verduras y frutos secos. Para armar el combo adecuado le consulta a sus clientes con que
    categoría desea armar el combo y cual es el precio máximo que quisiera pagar. Si fue verduras y el
    monto es mayor o igual a $10000, le ofrece Los mix de vegetales para ensaladas, pero si fue menor a
    $10000 le ofrece las bandejas de verduras para sopa. Si eligió otra categoría , le ofrece papas para el
    asado
"""
# No tiene sentido este ajsfjasxnasd
continua = input("Bienvenido a la B-erduleria de River, escriba si para continuar...").lower()
while continua == 'si':
    opcion = input("Desea conocer los combos disponibles? 'verduras u otros'si/no")
    
    if opcion == 'si':
        combo = input("\n indique que combo desea")
        if combo == 'verduras':
            dinero = int(input("\nIndique cuanto desea pagar: "))
            if dinero >= 10000:
                print("Podemos ofrecerle el mix de vegetables para ensaladas")
            elif dinero < 10000:
                print("le ofresco bandeja de verduras para sopa")
        elif combo == 'otro':
            print("Le ofrezco papas para el asado perro")
    
    else:
        print("Vuelva cuando quiera!")
        continua = 'no'

""" 
    3- En un supermercado se registran los productos más vendidos, y se consulta al cliente, para fomentar
    más ventas, si quiere conocer los productos más vendidos, si el cliente responde afirmativamente, le
    consulta sobre la categoría del producto (bazar, productos lácteos, productos de perfumería). En base a
    su respuesta de categoría mostrará: Para el bazar se muestra tazas, jarras y cubiertos. Para los lácteos
    leches , yogurt y queso. Y para la perfumería Jabón líquido, detergente y lavandina.
"""
opcion = input("Buenas tardes para ingresar presione 'si', para salir presione 'no' ")
while opcion == 'si':
    respuesta = input("Desea conocer los productos mas vendidos? si/no: ").lower()
    
    if respuesta == 'si':
        categoria = input("Que categoria desea ver?: Bazar, Lacteos o perfumeria?: ").lower()
        perf = ['perfumes', 'perfume', 'perfumeria']
        if categoria == 'bazar':
            print("tazas, jarras y cubiertos") 
        elif categoria == 'lacteos' or categoria == 'lacteo':
            print("leches , yogurt y queso")    
        elif categoria in perf:
            print("Jabón líquido, detergente y lavandina")
        
        opcion = input("Desea ver otra categoria? (si/no)").lower()
    else:
        print("Have a nice day!")
        opcion = 'no'
        
        
""" 
    4- La promoción de la pastelería ofrece que al llevar 3 productos se pague solamente el monto del
    producto más alto. Para eso, se le pide al cliente que ingrese los precios de los 3 productos y se le
    mostrará la leyenda Promoción! Se pagará por tres artículos: valor más alto
"""
productos = []
for i in range(3):
    var = int(input("ingrese el precio de sus productos: "))
    productos.append(var)
    
max_value = max(productos)

print(f"usted pagara por tres articulos: {max_value:.2f} $")

""" 
    5- La nueva promoción de las pastelería se basa en como los clientes ingresen los precios de los
    productos. Se les solicita ingresar el precio de cada uno de los 3 productos comprados. Si el orden de los
    ingresos es descendente , pagarán el total dividido 3. En cambio si el orden de ingreso es ascendente,
    pagarán el total de los productos divido 2. Se deberá mostrar Promoción!! Monto a pagar: y el valor
    según corresponda
"""
opcion = input("desea empezar? (si/no)").lower()
while opcion == 'si':
    try:
        valores = []
        
        for i in range(3):
            valor = int(input("Porfavor ingrese el precio de los productos"))
            valores.append(valor)
        
        ordenada = all(valores[i] <= valores[i+1] for i in range(len(valores)-1)) # algo nuevo como comprobar que esta ordenada
        print(f"¿La lista está ordenada?: {ordenada}")
        if ordenada: # es el valor implicito que devuelve pero si va true tambien esta bien
            suma = 0
            for i in range(len(valores)): # siempre recuerda que se pasa el tamaño de la lista no los valores como tal para que se sobre entienda el tamaño de donde debe partir
                suma += valores[i]
            #     suma = valores[i] + valores[i+1]
            # suma = sum(valores)     
            print(f"Promocion: $ {suma/3:.2f}")
        else:
            prom = 0
            for i in range(len(valores)):    
                prom += valores[i]
            
            print(f"el valor total sera {prom/2}")
            
        opcion = input("desea continuar? (si/no)")
    except ValueError:
        print("el tipo ingresado debe ser numerico")
        
opcion = input("desea continuar? (si/no)")
""" 
2- El local para sus clientes frecuentes les entrega una código promocional (LIFE) y otro código para el resto
de los clientes, mediante su app el cliente puede consultar si el código recibido por el local tiene el beneficio
de un descuento. Si el cliente ingresa otro código se le informará que el código no tiene beneficios, si es el
correcto se le informa un 20 % de descuento.
3-Para ingresar a la app de la tienda se le asigna a los clientes los códigos RRS o FT . Desarrolle el programa
que indique al usuario si el código es correcto Bienvenido!!! Si no lo es que lo intente de nuevo.
4-El hotel tiene un sistema para recolectar los comentarios del cliente en base a su estadía, le solicita que
ingrese sus comentarios y para terminar escriba la palabra off. Por cada comentario se le agradece y se le
indica que fueron aceptados. Se recibirán tantos comentarios como desee escribir hasta que escriba la
palabra off para indicar que ya no ingresará más.
5- Se desea armar un programa que le indique al cliente la totalidad de la compra previamente a pasar por
caja. Para ello se le solicita el Precio del siguiente artículo (0 para terminar de cargar). Una vez que haya
cargado todos los artículos se le mostrará Monto total de todas las compras:
"""
""" 
    1- Un local de comidas quiere informar sobre los horarios del local a sus clientes, el establecimiento
    permanece abierto entre las 10 am y las 00 pm, para ello si el cliente tiene dudas de si el local está abierto o
    no , le solicita que ingrese la hora actual, si está dentro del horario le informa Estamos Abiertos, caso
    contrario le informa Estamos cerrados. Nuestro horario de apertura es de 10:00 a.m. a medianoche.
    Desarrolle el programa que necesita el local.
"""


#  ejercicio 6
resu = input("Ingrese palabra: ").upper()

count = 0
while count < len(resu):
    print(resu[count])
    count += 1

resu = "el rosal".upper()

while resu:
    print(resu[0]) #toma el indice del caracter actual
    resu = resu[1:] #actualiza y se coloca en el siguiente la siguiente vez seria el caracter
""" 
7- Una nueva promoción en la farmacia pide juntar tickets de compra , al ingresar en la app se le solicita al cliente
Que cargue el monto total de cada ticket, cuando no tenga más ticket para cargar deberá ingresar como monto
0. El programa sumará todos los montos de los ticket y le dará al cliente un descuento del 10% sobre el total, i
Informando Su beneficio es de : valor del 10%

clase ultima while

2-La tienda de ropa quiere hacer una promoción y para eso va a premiar a los 3 primeros compradores
Del día con un descuento del 10%. Para ello, le solicita al cliente que ingrese su número de tarjeta, si es
De los 3 primeros le informa ¡Felicidades. Recibiste un descuento del 10%!, caso contrario se informa que
Ya no hay descuentos este día. Armar el programa que modele la promoción de la tienda.
3-Para ampliar las categorías del local, se le consulta al cliente que ingrese todas las categorías de los
Productos que compro de la siguiente manera Categoría (end - cuando termine de cargar):, cuando el
Cliente ingrese la palabra clave end, el programa deberá mostrarle
Número total de categorías de productos: cantidad
4-Para acceder al descuento , la empresa entrega a sus cliente el código FREE, y le da hasta 3 intentos
Para acceder a la página con el código de descuento. El programa debe pedirle al cliente que ingrese el
Código promocional otorgado y deberá mostrarle al final Aceptado en el intento #
5-La línea de colectivo coloco en sus cabeceras una máquina expendedora de boletos, la cual le informa
Al usuario 0 - obtener un boleto, 1 - apagar la máquina: Por cada boleto que solicita se le mostrará
número de boleto : el número asignado.
6- Para las compras con totales pares la heladería hace una promoción donde les cobra la mitad de lo
Que gastaron. Para ello los clientes ingresan el monto del ticket, si la mitad calculada también es par,
Vuelven a recibir la promoción, hasta que el monto sea impar
8- El supermercado quiere fomentar el consumo de ciertas categorías del negocio para eso le pide al
Cliente que ingrese la categoría de su preferencia Categoría (stop - cuando termine de cargar):
Si el cliente ingresa productos de carne se le hace un 10% de descuento en esa categoría, Si ingresa
Bebidas se le hace un 30% , para cualquier otra no hay descuentos. Se le deberá informar en la salida
El descuento correspondiente.
9- El supermercado consulta al sus clientes sobre las compras realizadas y les hace un descuento en
El momento. Les pide que ingresen Categoría (off - cuando termine de cargar): y el monto gastado.
Si son productos lácteos se le informa el descuento y el monto a pagar 10% de descuento. Monto a pagar:
Si fue pastelería 30% de descuento. Monto a pagar:
Cualquier otra categoría Sin descuento. Monto a pagar:
Una vez que ingresa Stop se le mostrará el mensaje de CAJA CERRADA
"""