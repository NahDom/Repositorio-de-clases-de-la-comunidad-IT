alumnos = ['Abrams', 'Khanna', 'Lee', 'Freeland', 'Qadiri']
cant_al = 0
opcion = input("desea empezar? (si/no): ")
if opcion.lower() != 'no':
    while True:
        ingreso = input("ingrese el nuevo alumno>> ")
        if ingreso.lower() == 'salir':
            break
        else:     
            alumnos.append(ingreso)
            cant_al = cant_al + 1
            print(f"la cantidad sumada de alumnos es:{cant_al}")
# los coloco en el orden correcto de salida
for i, elemento in enumerate(sorted(alumnos), start=1):
    print(i,'.',elemento)