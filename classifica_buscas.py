#home, busca, logado => comprou = 75% MultinomialNB
#home, busca, logado => comprou = 75% AdaBoostClassifier


# algoritmo que responde tudo 1 ou 0
def algoritmo_base(Y):
    from collections import Counter

    # total_de_acertos_burro_1 = list(Y).count(1)
    # total_de_acertos_burro_0 = len(Y[Y == 0])
    # Counter mostra os dados que aparecem e o max pega o que aparece mais
    total_de_acertos_base = max(Counter(Y).itervalues())
    taxa_de_acerto_base = 100.0 * total_de_acertos_base / len(Y)
    print('Taxa de acerto base: {}'.format(taxa_de_acerto_base))

#funcao para treinar e mostrar resultados
def fit_and_predict(nome, modelo, treino_x, treino_y, teste_x, teste_y, validacao_x, validacao_y):
    modelo.fit(treino_x, treino_y)

    resultado_teste = modelo.predict(teste_x)
    diferencas_teste = resultado_teste - teste_y

    acertos_teste = [d for d in diferencas_teste if d == 0]
    total_de_acertos_teste = len(acertos_teste)
    total_de_elementos_teste = len(teste_x)
    taxa_de_acerto_teste = 100.0 * total_de_acertos_teste / total_de_elementos_teste

    resultado_validacao = modelo.predict(validacao_x)
    diferencas_validacao = resultado_validacao - validacao_y
    acertos_validacao = [d for d in diferencas_validacao if d == 0]
    total_de_acertos_validacao = len(acertos_validacao)
    total_de_elementos_validacao = len(validacao_x)
    taxa_de_acerto_validacao = 100.0 * total_de_acertos_validacao / total_de_elementos_validacao

    print('\n-----{}-----'.format(nome))
    print('Total treinado: {}'.format(len(treino_x)))
    print('--TESTE--')
    print('Total de elementos: {}'.format(total_de_elementos_teste))
    print('Taxa de acerto: {}'.format(taxa_de_acerto_teste))
    algoritmo_base(teste_y)
    print('--VALIDACAO--')
    print('Total de elementos: {}'.format(total_de_elementos_validacao))
    print('Taxa de acerto: {}'.format(taxa_de_acerto_validacao))
    algoritmo_base(validacao_y)

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
porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1

tamanho_de_treino = int(porcentagem_de_treino * len(X))
tamanho_de_teste = int(porcentagem_de_teste * len(X))
tamanho_de_validacao = len(X) - tamanho_de_treino - tamanho_de_teste

treino_x = X[:tamanho_de_treino] #dados
treino_y = Y[:tamanho_de_treino] #marcacoes

fim_de_teste = tamanho_de_treino + tamanho_de_teste
teste_x = X[tamanho_de_treino:fim_de_teste] #dados
teste_y = Y[tamanho_de_treino:fim_de_teste] #marcacoes

validacao_x = X[fim_de_teste:] #dados
validacao_y = Y[fim_de_teste:] #marcacoes

from sklearn.naive_bayes import MultinomialNB
modelo_MultinomialNB = MultinomialNB()
fit_and_predict('MultinomialNB', modelo_MultinomialNB, treino_x, treino_y, teste_x, teste_y, validacao_x, validacao_y)

from sklearn.ensemble import AdaBoostClassifier
modelo_AdaBoostClassifier = AdaBoostClassifier()
fit_and_predict('AdaBoostClassifier', modelo_AdaBoostClassifier, treino_x, treino_y, teste_x, teste_y, validacao_x, validacao_y)

