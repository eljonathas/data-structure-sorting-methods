import os
import random as rd
import time

from src.insertion_sort import Insertion
from src.quick_sort import quick_sort
from src.radix_sort import radix_sort

execution = True

# Função para mudar a cor do texto


def parse_text_color(text, color):
    return f"\033[{color}m{text}\033[0m"

# Função para limpar o terminal


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


while execution:
    # Escolher uma opção
    print(parse_text_color(
        "1 - Radix Sort\n2 - Quick Sort\n3 - Insertion Sort\n4 - Sair do programa", "1;32"))
    option = int(input(parse_text_color("Escolha uma opção: ", "1;33")))
    clear_console()

    if option == 4:
        execution = False
        print(parse_text_color("Programa finalizado ❌", "1;31"))
        break

    # Escolher o tipo de ordenação
    print(parse_text_color(
        "Tipo de ordenação do vetor inicial:\n1 - Aleatório\n2 - Decrescente", "1;32"))
    option_sort = int(input(parse_text_color("Escolha uma opção: ", "1;33")))
    clear_console()

    # Escolher o tamanho do vetor
    array_size = int(input(parse_text_color(
        "Escolha o tamanho do vetor: ", "1;33")))

    # Vetor inicial
    generated_array = []

    # Se a opção de ordenação escolhida for aleatória, o vetor será gerado aleatoriamente
    if option_sort == 1:
        generated_array = [rd.randint(0, array_size)
                           for _ in range(array_size)]

    # Caso contrário, o vetor será gerado em ordem decrescente
    elif option_sort == 2:
        generated_array = [array_size - i for i in range(array_size)]

    if option == 1:
        print(parse_text_color("Radix Sort 🌄", "1;32"))

        # Inicia o tempo de execução
        start_time = time.time()

        # Cria um vetor cópia do vetor inicial
        initial_array = generated_array.copy()

        # Ordena o vetor
        sorted_array = radix_sort(generated_array)
        print(f"Vetor de entrada: {initial_array}")
        print(f"Vetor ordenado: {sorted_array}")
        print(f"Tempo de execução: {time.time() - start_time}")
        print()
    elif option == 2:
        print(parse_text_color("Quick Sort 👾", "1;32"))

        # Inicia o tempo de execução
        start_time = time.time()

        # Cria um vetor cópia do vetor inicial
        initial_array = generated_array.copy()

        # Ordena o vetor
        sorted_array = quick_sort(generated_array)
        print(f"Vetor de entrada: {initial_array}")
        print(f"Vetor ordenado: {sorted_array}")
        print(f"Tempo de execução: {time.time() - start_time}")
        print()
    elif option == 3:
        print(parse_text_color("Insertion Sort 🛸", "1;32"))

        # Inicia o tempo de execução
        start_time = time.time()

        # Cria um vetor cópia do vetor inicial
        initial_array = generated_array.copy()

        # Ordena o vetor
        sorted_array, comparisons, swap = Insertion(generated_array)
        print(f"Vetor de entrada: {initial_array}")
        print(f"Vetor ordenado: {sorted_array}")
        print(f"Quantidade de comparações: {comparisons}")
        print(f"Quantidade de trocas: {swap}")
        print(f"Tempo de execução: {time.time() - start_time}")
        print()
    else:
        print(parse_text_color("Opção inválida ⚠️", "1;31"))
