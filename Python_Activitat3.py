def llista():
# El usuario introduce por teclado un número del 1 al 20
    num = int(input("Introduce un número: "))
# Validamos si se ha introducido un número del 1 al 20
    while num > 20 or num < 1:
        num = int(input("Introduce un número del 1 al 20: "))
    return num

# Se printa el resultado de la operación
def multiplos(num):
    print([num * x for x in range(100) if (num * x) < 100])

def main():
    n = llista()
    multiplos(n)

if __name__ == "__main__":
   main()