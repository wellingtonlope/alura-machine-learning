from dados import carregar_acessos

x, y = carregar_acessos()

#10%
sep = int(len(x) * 0.1) - len(x)

treino_x = x[sep:]
treino_y = y[sep:]

teste_x = x[:sep]
teste_y = y[:sep]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(treino_x, treino_y)


resultado = modelo.predict(teste_x)
diferencas = resultado - teste_y
acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_x)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(taxa_de_acerto)