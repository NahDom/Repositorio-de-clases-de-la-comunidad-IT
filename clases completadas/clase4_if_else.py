""" 
1- La pastelería Sweet quiere ofrecer a sus clientes descuentos en próximas compras asignandole un código
de promoción. Si es la primera vez que visito la tienda se le asigna el código NEW y se le otorga un 40% de
descuento para la próxima compra. Si el cliente ya visito la tienda se le asigna el código CAKE y se le da un
10% de descuento en la compra de tortas. Crear un programa que muestre el tipo de código de promoción
y el descuento según el caso.
2- La pastelería quiere hacer sugerencias a sus cliente en base a lo quieran gastar en el local.
Si gastaría hasta $5000 se le ofrece la torta de leche, entre $5000 y $10000 inclusive el pastel de coco, más
de $10000 la torta Matilda. Armar el programa para que muestre la sugerencia según el importe a gastar.
3- La nutricionista del local propone sugerencias de postres a los clientes en base a su altura y peso. Si la
diferencia es mayor a 100 se le sugiere una medialuna rellena, caso contrario un mousse de arándanos.
Desarrolle el programa para realizar mostrar la sugerencia en base al calculo planteado.
4-Una heladería lleva una estadística de los sabores de helados que prefieren los clientes según su edad.
Para los menores de 30 años el sabor preferido es el helado de pistachos, mientras que los mayores de 30
prefieren el helado de chocolate amargo. Teniendo en cuenta la edad del cliente desarrolle el programa
que realice la sugerencia de sabor en su pedido.
5-Para un cumpleaños el cliente tiene la cantidad de kg que necesita para comprar un postre, espera que
en base ese valor la pastelería le sugiera el postre perfecto.
Si necesita hasta 2 kg se le ofrece las tartaletas de crema, si es entre 2 kg y 3 kg inclusive se le ofrece la torta
de mousse bañada, si es más de 3 kg la torta de 2 pisos con crema.
Realizar el programa que realice la sugerencia correspondiente según la cantidad de kilogramos.
6- Para realizar los presupuestos de tortas a medida , el cliente debe indicar el peso de la torta en gramos y
el tipo de relleno. La pastelería cobra para tortas hasta 2500 gramos $5500, superiores a ese peso $7000. Si
el relleno es de frutas se le agrega $1000, para el resto de los rellenos se añade $500. Mostrar el presupuesto
total del pedido
"""

""" 
1- La pastelería Sweet quiere ofrecer a sus clientes descuentos en próximas compras asignandole un código
de promoción. Si es la primera vez que visito la tienda se le asigna el código NEW y se le otorga un 40% de
descuento para la próxima compra. Si el cliente ya visito la tienda se le asigna el código CAKE y se le da un
10% de descuento en la compra de tortas. Crear un programa que muestre el tipo de código de promoción
y el descuento según el caso.
"""

cliente_respuesta = input("Usted ya ha visitado la tienda anteriormente?(si/no)\n")

def supermarket(cliente_respuesta):
    
    cliente_status = None
    
    if cliente_respuesta.lower() == 'no':
        cliente_status = 'Nuevo'
        return f"Como su respuesta fue: {cliente_respuesta}, su estado actual es de cliente: {cliente_status} y tiene un 40% en su proxima compra"
    else:
        cliente_status = 'Recurrente'
        return f"Como su respuesta es: {cliente_respuesta}, su estado es de cliente: {cliente_status} y tiene un 10% de descuento en la proxima compra"

print(supermarket(cliente_respuesta)) 
# siempre...coloca un print cuando llames a la funcion, bueno no siempre pero se entiende

""" 
    2- La pastelería quiere hacer sugerencias a sus cliente en base a lo quieran gastar en el local.
    Si gastaría hasta $5000 se le ofrece la torta de leche, entre $5000 y $10000 inclusive el pastel de coco, más
    de $10000 la torta Matilda. Armar el programa para que muestre la sugerencia según el importe a gastar.
"""

print(" ==== | Bienvenido | ==== \n")
print("Cuanto estaria dispuesto a pagar?: \n")
cliente_importe = int(input("Ingrese importe: "))

def pasteleria(cliente_importe):
    
    if cliente_importe <= 5000:
        return "pobre jsjsjsjs"
    elif cliente_importe > 5000:
        return "Podemos ofrecer hasta una torta de leche"
    elif cliente_importe >= 5000 and cliente_importe < 10000:
        return "hasta un pastel de coco te ofrezco"
    else:
        return "la torta de Matilda...es un pastel si" 
    
print(pasteleria(cliente_importe))

""" 
    3- La nutricionista del local propone sugerencias de postres a los clientes en base a su altura y peso. Si la
    diferencia es mayor a 100 se le sugiere una medialuna rellena, caso contrario un mousse de arándanos.
    Desarrolle el programa para realizar mostrar la sugerencia en base al calculo planteado.
"""


print(" ==== | Bienvenido | ==== \n")
altura = float(input("Ingrese su altura en cm: \n"))
peso = float(input("Ingrese su peso en kg: \n"))
peso_cliente = peso / altura
def IMC(peso_cliente):
    if (peso_cliente) > 100:
        return f"Su IMC es de {peso_cliente}, le podemos ofrecer una media luna rellena"
    else:
        return "Le ofrecemos un mousse de arandanos"
print(IMC(peso_cliente))


""" 
    4-Una heladería lleva una estadística de los sabores de helados que prefieren los clientes según su edad.
    Para los menores de 30 años el sabor preferido es el helado de pistachos, mientras que los mayores de 30
    prefieren el helado de chocolate amargo. Teniendo en cuenta la edad del cliente desarrolle el programa
    que realice la sugerencia de sabor en su pedido.
"""

print(" ==== | Bienvenido | ==== \n")
edad = int(input("Ingrese su edad: \n"))

if edad > 30:
    print("Chocolate amargo")
elif edad <= 30:
    print("Helado de gay")
    

""" 
    5-Para un cumpleaños el cliente tiene la cantidad de kg que necesita para comprar un postre, espera que
    en base ese valor la pastelería le sugiera el postre perfecto.
    Si necesita hasta 2 kg se le ofrece las tartaletas de crema, si es entre 2 kg y 3 kg inclusive se le ofrece la torta
    de mousse bañada, si es más de 3 kg la torta de 2 pisos con crema.
    Realizar el programa que realice la sugerencia correspondiente según la cantidad de kilogramos.
"""
print(" ==== | Bienvenido | ==== \n")
valor_peso = float(input("Ingrese el peso que necesita para el postre: \n"))
if valor_peso <= 2:
    print("tartaletas de crema")
elif valor_peso >=2 and valor_peso < 3:
    print("torta de mousse bañada")
else:
    print("torta de 2 pisos con crema")
    
""" 
    6- Para realizar los presupuestos de tortas a medida , el cliente debe indicar el peso de la torta en gramos y
    el tipo de relleno. La pastelería cobra para tortas hasta 2500 gramos $5500, superiores a ese peso $7000. Si
    el relleno es de frutas se le agrega $1000, para el resto de los rellenos se añade $500. Mostrar el presupuesto
    total del pedido
"""


print(" ==== | Bienvenido | ==== \n")
torta_peso = int(input("Ingrese peso en gramos: \n"))
relleno = input("Ingrese el relleno que desea ponerle: \n").lower()

if torta_peso <= 2500:
    precio = 5500
else:
    precio = 7000
    
if relleno == 'frutas':
    adicional = 1000
else:
    adicional = 500

total = precio + adicional

print(f"Peso de la torta {torta_peso}, relleno: {relleno}, Precio total: {total}")
# otra version con match case


# print(" ==== | Bienvenido | ==== \n")
# print("\n")
# torta_peso = int(input("Ingrese peso en gramos: \n"))
# relleno = input("Ingrese el relleno que desea ponerle: \n").lower()

# match (torta_peso, relleno):
#     case (peso, _) if peso <= 2500:
#         print("No podemos darte nada")
#     case (2500, 'frutas'):
#         print("valor de 5500")
#     case(peso, 'frutas') if peso > 2500:
#         print("Precio de 8000")
#     case(peso, _) if peso > 2500:
#         print("Precio de 7500")      

# if torta_peso <= 2500 and relleno == 'frutas:
#     print("El valor es de $6500 pesos")
# elif  torta_peso <  2500 and relleno != 'frutas':
#     print("El valor es de 6000$ pesos")
# elif torta_peso > 2500 and relleno == 'frutas':
#     print("El precio es de 8000$")
# elif torta_peso > 2500 and relleno != 'frutas':
#     print("El precio es de 7500$")