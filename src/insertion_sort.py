import random as rd
import time
import sys

comparacoes, atribuicoes = 0, 0
comparacoes_1, atribuicoes_1 = 0, 0


def insertion_sort_log():
    logs = []

    global comparacoes_1
    global atribuicoes_1

    # Test for list with 100 items
    array = [rd.randint(0, 100) for i in range(100)]
    start_time = time.time()
    Insertion_Inverse(array)
    end_time = time.time()
    logs.append([100, end_time - start_time, comparacoes_1, atribuicoes_1])

    # Test for list with 1000 items
    array = [rd.randint(0, 100) for i in range(1000)]
    start_time = time.time()
    Insertion_Inverse(array)
    end_time = time.time()
    logs.append([1000, end_time - start_time, comparacoes_1, atribuicoes_1])

    # Test for list with 10000 items
    array = [rd.randint(0, 100) for i in range(10000)]
    start_time = time.time()
    Insertion_Inverse(array)
    end_time = time.time()
    logs.append([10000, end_time - start_time, comparacoes_1, atribuicoes_1])

    # Test for list with 20000 items
    array = [rd.randint(0, 100) for i in range(20000)]
    start_time = time.time()
    Insertion_Inverse(array)
    end_time = time.time()
    logs.append([20000, end_time - start_time, comparacoes_1, atribuicoes_1])

    f = open("../logs/insertion_sort_log.txt", "w")

    f.write("Insertion Sort log: \n")
    f.write("N de elementos, Tempo, Comparacoes, Atribuicoes:\n")

    for i in range(len(logs)):
        f.write("{}, {}, {}, {}\n".format(
            logs[i][0], logs[i][1], logs[i][2], logs[i][3]))

    f.close()


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


insertion_sort_log()
