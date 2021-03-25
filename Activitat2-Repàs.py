def test(num):
    if num % 2 == 0:
        var = num / 5
    else:
        var = num * 2
    return int(var)

def main():
    lista = list()
    for x in range(1, 146):
        if test(x) % 2 == 0:
            lista.append(test(x))
    print(lista[5:])

if __name__ == "__main__":
    main()