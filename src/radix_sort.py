# Radix é um algoritmo de tempo linear destinado a ordenar números
# inteiros positivos. Ele é um dos algoritmos de ordenação mais rápidos
# que existe. O seu tempo de complexidade médio é O(k x n), sendo que  k
# é o número de dígitos significativos do maior número e n é o nnúmero de
# na lista. Ele possui possui uma complexidade espacial de O(n), pois é
# necessário espaço para armazenar cada balde
import time
import random

qtd_of_comparisons = 0
qtd_of_swaps = 0


def radix_sort_log():
    logs = []

    for i in range(20):
        # Teste com uma lista de 1000 números aleatórios
        random_list = [random.randint(0, 100) for i in range(1000)]
        start_time = time.time()
        radix_sort(random_list)
        logs.append([1000, time.time() - start_time])

    f = open("../logs/radix_sort_log.txt", "w")

    f.write("Radix sort logs:\n")
    f.write("Quantity of items, time\n")

    for log in logs:
        f.write(str(log[0]) + ", " + str(log[1]) + "\n")

    f.close()


def radix_sort(vetor):
    global qtd_of_comparisons
    global qtd_of_swaps

    # Ordena números inteiros de base 10
    base = 10
    # Serve como uma bandeira para saber quando a ordenação está completa
    concluido = False
    # Qual casa decimal se está ordenando agora
    casa_decimal = 1

    while(not concluido):
        concluido = True
        # Os baldes são criados como uma lista de listas
        # Como os números são de base 10, são necessárias 10 sublistas.
        baldes = [[] for _ in range(0, 10)]

        for numero in vetor:
            # Seleciona o algarismo da casa decimal do momento, por exemplo
            # unidades, centenas e dezenas
            parte_restante = numero // casa_decimal
            if parte_restante > 0:
                concluido = False

            # Seleciona qual o balde correto para este algarismo e
            # o adiciona no balde
            digito = parte_restante % base
            # Se algum dos números ainda tiverem dígitos desordenados,
            # continuar ordenando
            baldes[digito].append(numero)

        # A casa decimal é atualizada para a seguinte
        casa_decimal *= base
        # Todos os elementos do vetor são excluídos
        vetor.clear()

        # O vetor é novamente populado com os números que estão nos baldes
        for lista in baldes:
            for numero in lista:
                vetor.append(numero)

    return vetor


radix_sort_log()
