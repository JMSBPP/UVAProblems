from sys import stdin


#El stream de datos es una secuencia ordenada de stream = llaves, se hacen consultas sobre las llaves
# La informacion es cambiante(Conjunto dinamico):
## 1-Usuario ingresa solicitud sobre el conjunto de datos (¿Cual es el maximo, minimo?, etc)
## 2- Solicitud tiene (0<=ID<=3000) y Period (0<=Period<=3000) intervalo de segundos entre dos retornos del resultado
## de la solicitud con su resp ID

## PARAMETROS:
## Todas las solictitudes tienen diferente ID

## Algoritmo/Funcion - Output
## El ID de las primeras K consultas en retornar resultado
#  Casos Borde:
# Si dos consultas se ejecutarian al tiempo retornar ID`S en orden ascendente


#Simulacion:
##Una vez entra mi trabajo


def right(i):
    return 2 * i + 1

def left(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def heap_increase_key(lista, indice, valor):
    if valor < lista[indice][0]:
        raise ValueError("key is smaller than current key")
    lista[indice][0] = valor
    while indice > 0 and lista[parent(indice)][0] < lista[indice][0]:
        lista[parent(indice)][0], lista[indice][0] = lista[indice][0], lista[parent(indice)][0]
        lista[parent(indice)][1], lista[indice][1] = lista[indice][1], lista[parent(indice)][1]
        indice = parent(indice)

def min_heapify(lista, indice):
    heap_size = len(lista)
    while True:
        r, l = right(indice), left(indice)
        min = indice

        if l < heap_size and lista[l][0] < lista[min][0]:
            min = l
        if r < heap_size and lista[r][0] < lista[min][0]:
            min = r

        if min != indice:

            lista[indice][0], lista[min][0] = lista[min][0], lista[indice][0]
            lista[indice][1], lista[min][1] = lista[min][1], lista[indice][1]
            indice = min
    
        else:
            break
    valor_min = lista[0]
    i=1
    while True:
        if valor_min[0]==lista[i][0] and valor_min[1] >lista[i][1]:
            lista[0], lista[i] = lista[i], lista[0]
        i+=1
        if i==heap_size:
            break

def build_heap(lista):
    heap_size = len(lista)
    for i in range(heap_size // 2 - 1, -1, -1):
        min_heapify(lista, i)
    return lista


    
def impresion(k,consultas, sumador):
    for i in range(k):
        build_heap(consultas)
        print(consultas[0][1])
        consultas[0][0] += sumador[consultas[0][1]]
        heap_increase_key(consultas,0,consultas[0][0])
        build_heap(consultas)
        
        



def main():
    trabajos=[]
    periods=[]
    while True:
        consulta = stdin.readline().strip().split()
        if consulta[0]=="#":
            break
        trabajos.append(int(consulta[1]))
        periods.append(int(consulta[2]))
    k = int(stdin.readline().strip())
    consultas = [list(pair) for pair in zip(periods, trabajos)]
    sumador = dict(zip(trabajos,periods))
    impresion(k,consultas, sumador)     
    print()  
main()
