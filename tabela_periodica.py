# Criar um menu para o aplicativo que permita:
# Listar todos os dados de todos os elementos inseridos (a ordem não importa, pois estamos usando dicionário).
# Listar todos os dados de determinado elemento, buscando através do seu símbolo [usar a busca por chave dos dicionários].
# Listar dados de determinado elemento, buscando através do seu símbolo [usar a busca por chave dos dicionários], porém
# solicitando ao usuário qual dado ele deseja ver (ex.: nome, número, …).

import csv

tabela_periodica = {}
estados = {'l': 'Líquido', 'g': 'Gasoso', 's': 'Sólido'}
tabela = {}

arq = csv.reader(open('tabela.txt'), delimiter=';')
for i, dado_linha in enumerate(arq):
    if i == 0:  # pula linha do cabecalho (1a linha do arquivo)
        continue

    dados = {}
    dados['simbolo'] = dado_linha[0]
    dados['nome'] = dado_linha[1]
    dados['atomico'] = dado_linha[2]
    dados['linha'] = dado_linha[3]
    dados['coluna'] = dado_linha[4]
    dados['estado'] = dado_linha[5]

    tabela[i] = dados
    tabela_periodica[dados['simbolo']] = dados

# print(tabela_periodica['Hg'])
# print(tabela_periodica['Na'])

resposta = input(
    'O que você deseja? a => listar todos os elementos, b => procurar um elemento e listar tudo sobre ele ou c=> buscar por um elemento e escolher a informação que deseja: ')


def verificaResposta():
    if respostaCerta == True:
        print(tabela_periodica[i])
    else:
        ('Esse elemento não exista na nossa base de dados...')


def verificaElemento():
    if respostaCerta == True:
        dado = input('Qual dado? ')
        if dado == 'simbolo':
            print(tabela_periodica[i]["simbolo"])
        elif dado == 'nome':
            print(tabela_periodica[i]["nome"])
        elif dado == 'atomico':
            print(tabela_periodica[i]["atomico"])
        elif dado == 'linha':
            print(tabela_periodica[i]["linha"])
        elif dado == 'coluna':
            print(tabela_periodica[i]["coluna"])
        elif dado == 'estado':
            print(tabela_periodica[i]["estado"])
            print(estados[tabela_periodica[i]["estado"]])
        else:
            print('Esse tipo de dado não existe...')
    else:
        ('Esse elemento não exista na nossa base de dados...')


if resposta == 'a':
    print(tabela_periodica)
elif resposta == 'b':
    tabela_elementos = ", ".join([str(_) for _ in tabela_periodica])
    tabela_elementos_list = list(tabela_elementos.split(', '))
    elemento = input('Qual elemento? ')
    for i in tabela_elementos_list:
        if elemento == i:
            respostaCerta = True
            verificaResposta()
        else:
            respostaCerta = False
            verificaResposta()
elif resposta == 'c':
    tabela_elementos = ", ".join([str(_) for _ in tabela_periodica])
    tabela_elementos_list = list(tabela_elementos.split(', '))
    elemento = input('Qual elemento? ')
    for i in tabela_elementos_list:
        if elemento == i:
            respostaCerta = True
            verificaElemento()
        else:
            respostaCerta = False
            verificaElemento()
else:
    print('Essa opção não é válida...')


# ACESSANDO OS DADOS DO ELEMENTO Hg
# elemento = tabela_periodica['Hg']
# print("--------")
# print(elemento['simbolo'])
# print(elemento['nome'])
