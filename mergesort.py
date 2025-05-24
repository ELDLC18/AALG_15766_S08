def mergesort(array):
    #Se comprueba si la lista es de 1 elemento
    if len(array) <= 1:
        return array
    
    #Se divide el arreglo a la mitad
    medio = len(array) // 2
    inicio = mergesort(array[:medio])
    fin = mergesort(array[medio:])

    #Se combina las dos mitades ordenadas
    return merge(inicio, fin)

def merge(izq, der):
    resultado = []
    i = j = 0

    #Se compara y combina los elementos ordenados
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    #Se agrega los elementos restantes si los hay, porque ya están ordenados
    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado 

lista = [6,12,14,7,2,9,11,3]
print(mergesort(lista))

