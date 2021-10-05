comparacoes, atribuicoes = 0, 0
comparacoes_1, atribuicoes_1 = 0, 0


def Insertion(array):
    global comparacoes
    global atribuicoes

    for index in range(1, len(array)):
        current_element = array[index]
        i = index - 1
        while i >= 0:
            comparacoes += 1
            if current_element < array[i]:
                array[i + 1] = array[i]
                array[i] = current_element
                atribuicoes += 2
                i -= 1
            else:
                break


def Insertion_Inverse(array):
    global comparacoes_1
    global atribuicoes_1

    for index in range(1, len(array)):
        current_element = array[index]
        i = index - 1
        while i >= 0:
            comparacoes_1 += 1
            if current_element > array[i]:
                array[i + 1] = array[i]
                array[i] = current_element
                atribuicoes_1 += 2
                i -= 1
            else:

                break
