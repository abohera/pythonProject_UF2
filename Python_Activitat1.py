# Definimos la función "llista"
def llista():
# El usuario introduce por teclado el número de registros que va a introducir
    size = int(input("¿Cuántos números vas a introducir?: "))
# Declaramos la lista que vamos a usar
    this_list = list()
    count = 0
# Estructura de repetición que pide al usuario un número y almacena la suma en la variable "count"
    for i in range(size):
        num = int(input("Introduce un número: "))
        this_list.append(num)
        count = this_list[i] + count
# Muestra por pantalla el resultado obtenido
    print(("\nLa suma total de todos los valores introducidos es: %d") % (count))

def main():
    llista()

if __name__ == "__main__":
   main()