""" clase 3 """
""" 1-A un grupo de estudiantes se les asigno la contraseña grupo1258 para ingresar en la plataforma
De la escuela. Realizar un programa para autenticar las contraseñas de este grupo solicitando que
introduzca la contraseña para iniciar sesión con su cuenta personal: y devolverles el mensaje Autorización: True o False
Según sea el caso.
2- En una pastelería el producto que más se vende son las tortas de chocolate, para llevar una estadística
De sus productos , hace un cuestionario a sus clientes sobre su última compra preguntando ¿Qué producto
Compro ? Y ¿ De que sabor ? En base a estos datos se debe mostrar Se compro el producto más vendido: True
O False según corresponda.
3- La pastelería tiene todos los días tortas en promoción a $4500. Para ofrecerle a sus clientes dichas promociones
Los consulta por su producto favorito y cuanto pagaría por el . Para aquellos clientes que coincidan en el producto
Y precio , deberá aparecer el mensaje de Ofrecer producto en promoción: True  para los que no coincidan se
Mostrará en mismo mensaje pero con False.
4- En la panadería están fabricando productos sin azúcar, libre de gluten y 0% contenido de grasa. Para conocer
Las posibles ventas dentro de sus clientes se les solicita que introduzcan si tienen alguna preferencia o restricción
Alimenticia. En base a lo ingresado si coincide con alguno de estos nuevos productos , el programa mostrará
Ofrecer productos dietéticos: True o false.
5- Dentro de la pastelería se realizan galletitas de varios sabores, las más consumidas son las de crema y las de
Mermelada. Para saber si los clientes las siguen eligiendo se los consulta en una breve encuesta.
¿Qué tipo de producto es de su preferencia? Y ¿Qué tipo de relleno? . En base a los datos recibidos se debe mostrar
La elección fue de las galletitas con relleno más vendidas: True o False
6- Para sugerir a sus clientes un nuevo producto, la pastelería debe conocer si sus clientes son alérgicos y en el caso
De serlo si es a la leche o el gluten. Para ello se deberá crear un programa que consulte a los clientes sobre estas
Cuestiones y muestre Tiene una alergia: True o false y Ofrecer nuevo producto: True o False. """


# 1-A un grupo de estudiantes se les asigno la contraseña grupo1258 para ingresar en la plataforma
# De la escuela. Realizar un programa para autenticar las contraseñas de este grupo solicitando que
# introduzca la contraseña para iniciar sesión con su cuenta personal: y devolverles el mensaje Autorización: True o False
# Según sea el caso.
contraseña = "grupo1258"

ingreso = input("Por favor ingrese la contraseña:\n")

def entrada(contraseña):
    if ingreso == contraseña:
        return True
    else:
        return False
    
print(entrada(contraseña))

# 2- En una pastelería el producto que más se vende son las tortas de chocolate, para llevar una estadística
# De sus productos , hace un cuestionario a sus clientes sobre su última compra preguntando ¿Qué producto
# Compro ? Y ¿ De que sabor ? En base a estos datos se debe mostrar Se compro el producto más vendido: True
# O False según corresponda.

pasteleria_op = input("Por favor, diganos cual fue el producto que mas compro:\n").lower()
estadistica = "torta de chocolate" in pasteleria_op # asi como el SQL es mas sencillo decirle si esta o no en el texto para que tanto...
print("Se compro el mas vendido:",estadistica)

