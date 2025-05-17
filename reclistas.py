#Haga una funcion recursiva que obtenga la suma de los elementos de una lista

#wrapper
def sumaLista(arr):
    if len(arr) > 0:
        return suma(arr, len(arr)-1)
    else:
        return 0

#funcion recursiva
def suma(arr, x) -> int:
    if x == 0:
        return arr[0]
    else:
        return arr[x] + suma(arr, x - 1)
    
def sumaLista(arr):
    if len(arr)>0:
        return suma2(arr, 0, len(arr)-1)
    else:
        return 0

def suma2(arr, x, n) -> int:
    if x == n:
        return arr[n]
    else:
        return arr[x] + suma2(arr, x+1)


lista = [5,8,7,2]

z = sumaLista(lista)
print(z)