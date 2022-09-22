import fabrica


def main ():
    fabricas = []
    produtos = [0, 1, 2]
    for i in range(0, 70):
        fabricas.append(fabrica.Fabrica(i, produtos))
        fabricas[i].subscribe()
        for u in produtos:
            u += 3
    while True:
        for i in fabricas:
            i.listen()

if __name__ == '__main__':
    main()
