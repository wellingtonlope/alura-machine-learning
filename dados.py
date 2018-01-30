import csv

def carregar_acessos():
    x = []
    y = []

    arquivo = open('acesso_pagina.csv', 'rb') #rb: leitura e retorno para a variavel
    leitor = csv.reader(arquivo)

    leitor.next()

    for home, como_funciona, contato, comprou in leitor:
        dado = [int(home), int(como_funciona), int(contato)]
        x.append(dado)
        y.append(int(comprou))

    return x, y

def carregar_buscas():
    x = []
    y = []

    arquivo = open('busca.csv', 'rb')
    leitor = csv.reader(arquivo)

    leitor.next()

    for home, busca, logado, comprou in leitor:
        dado = [int(home), busca, int(logado), int(comprou)]
        x.append(dado)
        y.append(int(comprou))

    return x, y