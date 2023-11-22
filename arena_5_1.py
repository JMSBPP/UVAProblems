from sys import stdin


def main():
    n = int(stdin.readline().strip())
    for _ in range(n):
        lista = [int(x) for x in stdin.readline().strip().split(' ')]
        trabajos, posicion_mi_trabajo  = lista[0], lista[1]
        prioridades = [int(x) for x in stdin.readline().strip().split(' ')]
        posiciones = [i for i in range(len(prioridades))]
        a_imprimir = max(prioridades)
        tiempo = 1 
        while len(prioridades) > 0:
            a_imprimir = max(prioridades)
            if prioridades[0] == a_imprimir and posiciones[0]!=posicion_mi_trabajo:
                prioridades.pop(0)
                posiciones.pop(0)
                tiempo+=1
            elif prioridades[0] != a_imprimir:
                x= prioridades.pop(0)
                y = posiciones.pop(0)
                prioridades.append(x)
                posiciones.append(y)
            elif prioridades[0] == a_imprimir and posiciones[0]==posicion_mi_trabajo:
                break
        print(tiempo)
            

main()