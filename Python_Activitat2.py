def llista():
# Declaramos la lista
    a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# Elimina los valores repetidos dentro de la lista
    a = list(set(a))
# Muestra por pantalla el resultado obtenido
    print(a)

# Ejecutamos la función creada anteriormente
def main():
    llista()

if __name__ == "__main__":
   main()