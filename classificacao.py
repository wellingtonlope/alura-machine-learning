# coding=utf-8
# é gordo? tem perna curta? faz auau?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
#treinando
modelo.fit(dados, marcacoes)

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
testes = [misterioso1, misterioso2, misterioso3]
marcacoes_test = [-1, 1, -1]

resultado = modelo.predict(testes)
print(resultado)

diferencas = resultado - marcacoes_test
# se 0 ele acertou, se -2 ou 2 ele errou
print(diferencas)

#total de acertos
acertos = [d for d in diferencas if d == 0]
print(acertos)
total_de_acertos = len(acertos)
print(total_de_acertos)
total_de_elementos = len(testes)
print(total_de_elementos)
taxa_de_acertos = 100.0 * total_de_acertos / total_de_elementos
print(taxa_de_acertos)

#saber total de erros
erros = [erro for erro in diferencas if erro != 0]

