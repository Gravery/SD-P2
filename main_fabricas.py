import fabrica

#Criação de 70 fábricas que ouvirão requisições de seus respectivos produtos
def main ():
    fabricas = []
    produtos = [0, 1, 2]
    print('Realizando conexão das 70 fábricas:\n')
    for i in range(0, 70):
        fabricas.append(fabrica.Fabrica(i, produtos.copy()))
        fabricas[i].subscribe()
        print(f'Fabrica {i} criada')
        for j in range(3):
            produtos[j] += 3

    while True:
        for i in fabricas:
            i.listen()

if __name__ == '__main__':
    main()
