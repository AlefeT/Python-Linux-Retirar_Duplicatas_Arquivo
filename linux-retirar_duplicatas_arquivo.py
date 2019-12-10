#!/usr/bin/python3
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - [ Bloco de Importar Bibliotecas (libs) ] - - - - - - - - - - - - - - #

try:
    import os

except Exception as E:
    print('Erro ao Importar Bibliotecas: ' + E)


# - - - - - - - - - - - - - - [ Bloco de Definicao de Variaveis (1o) ] - - - - - - - - - - - - - - #

# [ Define as Variaveis ]
try:
    arquivoBase = 'teste.txt'  # Define o arquivo a partir do qual sera gerado uma copia sem as linhas duplicatas

except Exception as E:
    print('Erro ao Definir as Variaveis: ' + E)


# - - - - - - - - - - - - - - [ Bloco de Execucao (2o) ] - - - - - - - - - - - - - - #

# [ Gera a copia sem linhas duplicatas do arquivo definido e abre o novo arquivo ]
try:
    # Gera a copia sem linhas duplicatas
    os.system('sort -u _BASES/' + arquivoBase + ' > _BASES/2' + arquivoBase)
    os.remove('_BASES/'+arquivoBase)
    arquivoBase = '2'+arquivoBase

    # Abre o novo arquivo e guarda o conteudo do mesmo na variavel 'data'
    data = open(arquivoBase, encoding="utf-8", errors='ignore').readlines()

except Exception as E:
    print('Erro ao Listar Arquivos: ' + E)
