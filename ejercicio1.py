#crear una funcion recursiva que me de la resta de la suma de los pares 
#menos los impares de una lista

def sumaresta(arr, x) -> int:

    if x == 0:
        return arr[0]
    else:
        if arr[x] % 2 == 0:
            return arr[x] + sumaresta(lista, x - 1)
        else:
            return -arr[x] + sumaresta(lista, x - 1)

lista = [2,3,8,1]
z = sumaresta(lista, len(lista)-1) #10-4=6
print(z)
