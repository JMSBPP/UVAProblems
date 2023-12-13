from sys import stdin


# captura los copos de nieve a medida que caen y los serializa en una corriente de copos de nieve que fluyen,
# uno por uno, en un paquete


# cada copo de nieve en UN paquete debe ser diferente de los demás.
# Pueden haber copos iguales pero en diferentes paquetes

#MUCHOS COPOS DE NIEVE SON IDENTICOS EL UNO AL OTRO


# TAMAÑO DEL PAQUETE MAS GRANDE POSIBLE DE COPOS DE NIEVE UNICOS QUE SE PUEDE CREAR


# Una vez que La máquina comienza  a llenar el paquete, todos los copos de nieve que fluyen de la máquina.
# debe entrar en el paquete hasta que el paquete esté completo y sellado. 


# El paquete se puede completar.
# y sellar antes de que todos los copos de nieve hayan salido de la máquina.


# Dos copos de nieve don identicos SI Y SOLO SI  se identifican con el mismo número entero


# OUTPUT: número máximo de copos de nieve únicos
# que pueden estar en un paquete

from icecream import ic

from sys import stdin

def main():
    casos = int(stdin.readline().strip())

    for _ in range(casos):
        bags = int(stdin.readline().strip())
        length = 0
        max_package = 0
        repeated_package = 0
        snowflakes = {}

        for i in range(1, bags + 1):
            serial = int(stdin.readline().strip())
            seen = snowflakes.get(serial, 0)
            ic(snowflakes)

            if seen:
                repeated_package = max(repeated_package, seen)
                length = i - repeated_package - 1

            length += 1
            ic(length)
            snowflakes[serial] = i
            ic(snowflakes)
            max_package = max(max_package, length)
            ic(max_package)

        print(max_package)

main()
