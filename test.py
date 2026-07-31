mi_lista = [1, 2, 3, 4, 5]
ordenada = all(mi_lista[i] <= mi_lista[i+1] for i in range(len(mi_lista) - 1))

print(ordenada) # Devuelve True


lista = [2,30,400]
orden = all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

for i in range(3):
    lista.append(i)
    
print(lista)