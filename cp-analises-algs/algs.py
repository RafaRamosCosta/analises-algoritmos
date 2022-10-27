# Rafael Ramos Costa RM94281 / Leonardo Ramos Costa RM94286

import time

# importando a biblioteca random para gerar a lista com números aleatórios
from random import randint

def get_time(algoritmo, lista, *args):
    '''
    Função get_time() - obtém a diferença entre duas medições de tempo (em segundos) de um programa/
    função.
    Parâmetros:    
        arg: função que será executada
    Retorno:    
        fim-inicio: diferença de tempo entre duas medições
'''
    inicio = time.time()
    algoritmo(lista, *args) # onde será chamada a função de ordenação
    fim = time.time()
    return fim-inicio

def cria_lista(t):
    '''
    Função cria_lista() - cria uma lista de números inteiros aleatórios .
    Parâmetros:
        t: tamanho da lista
    Retorno:
        lista: lista de números inteiros aleatórios
    '''
    lista = []
    for i in range(t):
        i = randint(0, 10000)
        lista.append(i)
    return lista
  
def escreve_lista(lista, nm_arq):
    '''
    Função escreve_lista() - função que escreve a lista em um arquivo.
    Parâmetros:
        lista: lista de números inteiros aleatórios
    Retorno:
        Nenhum
    '''
    lista_retorno = []
    for i in range(len(lista)):
      lista[i] = str(lista[i])
      lista_retorno.append(lista[i])
      lista_retorno.append(',')
    lista_retorno.append('\n')
    with open(str(nm_arq), 'a') as file:
        file.writelines(lista_retorno)
        file.close()
        

def escolha_algoritmo(): 
    '''
    Função escolha_algoritmo() - função que captura a escolha do usuário em relação a que algoritmo irá utilizar.
    Parâmetros:
        Nenhum
    Retorno:
        escolha: escolha do usuário
    '''
    escolha = int(input("Escolha o algoritmo:\n (1) Bubble Sort\n(2) Selection Sort\n(3) Insertion Sort\n(4) Merge Sort\n(5) Quick Sort "))
    return escolha

def le_arquivo(nm_arquivo):
    '''
    Função le_arquivo() - função que lê um arquivo e retorna seu conteúdo.
    Parâmetros:
        nm_arquivo: nome do arquivo a ser lido
    Retorno:
        dados: dados do arquivo
    '''
    with open(nm_arquivo, 'r') as file:
        lista = []
        dados = file.read().split(',')
        dados.pop()
        for i in range(len(dados)):
          dados[i] = int(dados[i])
        for el in dados:
          lista.append(el)
        file.close()
        return lista
        

def executa_algoritmos(escolha, lista):
    '''
    Função executa_algoritmos() - função que executa o algoritmo escolhido pelo usuário.
    Parâmetros:
        escolha: escolha do usuário
        lista: lista de números inteiros aleatórios desordenados
    Retorno:
        Nenhum
    '''
    if escolha == 1:
        bubble_sort(lista)
    elif escolha == 2:
        selection_sort(lista)
    elif escolha == 3:
        insertion_sort(lista)
    elif escolha == 4:
        merge_sort(lista)
    elif escolha == 5:
        quick_sort(lista)
    else:
        print("Opção inválida!")
    


def bubble_sort(lista):
    '''
    Função bubble_sort() - função que utiliza o algoritmo de ordenação bubble sort para 
    ordenar a lista passada como parâmetro.

    Parâmetros:
        lista: lista desordenada de números inteiros
    Retorno:
        lista: lista ordenada de números inteiros
    '''
    t = len(lista)
    for i in range(len(lista)):
        while t > 1:
            for j in range(len(lista)-1):
                if(lista[j] > lista[j+1]):
                    lista[j], lista[j+1] = lista[j+1], lista[j] 
            t -= 1
                

def selection_sort(lista):
    '''
    Função selection_sort() - função que implementa o algoritmo de ordenação selection sort para 
    ordenar a lista passada como parâmetro.
    
    Parâmetros:
        lista: lista desordenada de números inteiros
    Retorno:
        nenhum
    '''
    for i in range(len(lista)):
        menor = i # menor recebe o índice do primeiro elemento da lista
        for j in range(i+1, len(lista)):   # percorre a lista a partir do segundo elemento
            if lista[j] < lista[menor]:     
                menor = j   # menor recebe o índice do menor elemento da lista no momento
        lista[i], lista[menor] = lista[menor], lista[i]  # troca o menor elemento com o anterior


def insertion_sort(lista):
    '''
    Função insertion_sort() - função que implementa o algoritmo de ordenação insertion sort para 
    ordenar a lista passada como parâmetro.
    
    Parâmetros:
        lista: lista desordenada de números inteiros
    Retorno:
        nenhum
    '''
    # inicia no 1 para comparar com o primeiro elemento da lista
    for i in range(1, len(lista)):
        pivo = lista[i]
        
        j = i - 1 # elemento anterior ao pivo   
        while j >= 0 and pivo < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = pivo
    
def merge_sort(lista):
    
    if len(lista) > 1:
        # encontra o meio da lista
        meio = len(lista) // 2
        # divide a lista em duas partes
        esquerda = lista[:meio]
        direita = lista[meio:]

        # chama a função recursivamente para cada metade 
        merge_sort(esquerda)
        merge_sort(direita)

        # definindo iteradores para as duas metades
        i = j = k = 0

        # valida se ainda existem elementos para trocar
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

def particao(lista, low, high):
    '''
    Funcão particao() - Essa função é responsável por encontrar a posição da partição.
    Parâmetros:
        lista - Lista de números inteiros
        low - Índice do primeiro elemento da lista
        high - Índice do último elemento da lista
    Retorno:
        i - Índice da partição
    '''
    pivo = lista[high]

    i = low - 1
 
    for j in range(low, high):
        if lista[j] <= pivo:
            i = i + 1
            (lista[i], lista[j]) = (lista[j], lista[i])
    (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
    return i + 1

def quick_sort(lista, low, high):
    '''
    Função quickSort() - Essa função é responsável por ordenar uma lista.
    Parâmetros:
        lista - Lista de números inteiros
        low - Índice do primeiro elemento da lista
        high - Índice do último elemento da lista
    Retorno:
        Essa função não retorna nenhum valor.
    '''
    if low < high:
        pi = particao(lista, low, high)
        quick_sort(lista, low, pi - 1)
        quick_sort(lista, pi + 1, high)

# def armazena_listas():
#     lista1 = cria_lista(1000)
#     lista5 = cria_lista(5000)
#     lista10 = cria_lista(10000)
#     lista50 = cria_lista(50000)
#     lista100 = cria_lista(100000)
#     escreve_lista(lista1, 'lista1.txt')
#     escreve_lista(lista5, 'lista5.txt')
#     escreve_lista(lista10, 'lista10.txt')
#     escreve_lista(lista50, 'lista50.txt')
#     escreve_lista(lista100, 'lista100.txt')

# armazena_listas()

