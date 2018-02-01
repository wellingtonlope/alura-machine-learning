#home, busca, logado => comprou = 75% MultinomialNB
#home, busca, logado => comprou = 75% AdaBoostClassifier

#funcao para treinar e mostrar resultados
def fit_and_predict(nome, modelo, treino_x, treino_y, teste_x, teste_y):
    modelo.fit(treino_x, treino_y)

    resultado = modelo.predict(teste_x)
    diferencas = resultado - teste_y

    acertos = [d for d in diferencas if d == 0]
    total_de_acertos = len(acertos)
    total_de_elementos = len(teste_x)
    taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

    print('\n-----{}-----'.format(nome))
    print('Total de testes: {}'.format(total_de_elementos))

    print('Machine Learning')
    print('Taxa de acerto: {}'.format(taxa_de_acerto))

    # algoritmo que responde tudo 1 ou 0
    print('Algoritmo base')
    from collections import Counter
    # total_de_acertos_burro_1 = list(Y).count(1)
    # total_de_acertos_burro_0 = len(Y[Y == 0])
    # Counter mostra os dados que aparecem e o max pega o que aparece mais
    total_de_acertos_base = max(Counter(teste_y).itervalues())
    taxa_de_acerto_base = 100.0 * total_de_acertos_base / len(teste_y)
    print('Taxa de acerto: {}'.format(taxa_de_acerto_base))

import pandas as pd

#lendo .csv
df = pd.read_csv('busca2.csv')
#pegando dados
X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

#transformando dados categoricos em dummies
Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = pd.get_dummies(Y_df)[1] #or Y_df

#df para array
X = Xdummies_df.values
Y = Ydummies_df.values

#treino 90% e 10% de treino
porcentagem_de_treino = 0.9
tamanho_de_treino = int(porcentagem_de_treino * len(X))
tamanho_de_teste = len(X) - tamanho_de_treino

treino_x = X[:tamanho_de_treino] #dados
treino_y = Y[:tamanho_de_treino] #marcacoes

teste_x = X[-tamanho_de_teste:] #dados
teste_y = Y[-tamanho_de_teste:] #marcacoes

from sklearn.naive_bayes import MultinomialNB
modelo_MultinomialNB = MultinomialNB()
fit_and_predict('MultinomialNB', modelo_MultinomialNB, treino_x, treino_y, teste_x, teste_y)

from sklearn.ensemble import AdaBoostClassifier
modelo_AdaBoostClassifier = AdaBoostClassifier()
fit_and_predict('AdaBoostClassifier', modelo_AdaBoostClassifier, treino_x, treino_y, teste_x, teste_y)

