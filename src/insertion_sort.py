comparacoes, atribuicoes = 0, 0
comparacoes_1, atribuicoes_1 = 0, 0


# Implementa o método de ordenação Insertion de forma ascendente
def Insertion(array):
    global comparacoes
    global atribuicoes

    for index in range(1, len(array)):
        # armazena o elemento atual que será comparado com o do lado
        elemento_atual = array[index]
        # armazena o indice do elemento a esquerda do atual
        i = index - 1

        while i >= 0:

            # incrementa um no contador de comparação
            comparacoes += 1
            # Se o elemento atual for menor do que o elemento a esquerda, eles trocam de posicao
            if elemento_atual < array[i]:
                array[i + 1] = array[i]
                array[i] = elemento_atual

                # O contador de atribuição é incrementado duas vezes, já que ocorrem duas atribuições por comparação
                atribuicoes += 2

                # Decrementa indice de referência para a comparação até a posição 0
                i -= 1
            else:
                break

    # retorna o array ordenado
    return [array, comparacoes, atribuicoes]
