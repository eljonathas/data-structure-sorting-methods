import os
import random as rd
import time

from src.insertion_sort import Insertion, Insertion_Inverse
from src.quick_sort import quick_sort, quick_sort_desc
from src.radix_sort import radix_sort

execution = True


def parse_text_color(text, color):
    print(f"\033[{color}m{text}\033[0m")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


while execution:
    # Escolher uma opção
    parse_text_color(
        "1 - Radix Sort\n2 - Quick Sort\n3 - Insertion Sort", "1;32")
    option = int(input("Escola uma opção: "))
    clear_console()

    # Escolher o tipo de ordenação
    parse_text_color(
        "Tipo de ordenação:\n1 - Ascendente\n2 - Descendente", "1;32")
    option_sort = int(input("Escola uma opção: "))
    clear_console()

    # Escolher o tamanho do vetor
    array_size = int(input("Escolha o tamanho do vetor: "))

    # Gerar o vetor
    generated_array = [rd.randint(0, 100) for _ in range(array_size)]

    if option == 1:
        parse_text_color("Radix Sort", "1;33")

        if option_sort == 1:
            start_time = time.time()
            sorted_array = radix_sort(generated_array)
            print(f"Vetor ordenado: {sorted_array}")
            print(f"Tempo de execução: {time.time() - start_time}")
    elif option == 2:
        parse_text_color("Quick Sort", "1;33")

        if option_sort == 1:
            start_time = time.time()
            sorted_array = quick_sort(generated_array)
            print(f"Vetor ordenado: {sorted_array}")
            print(f"Tempo de execução: {time.time() - start_time}")
        else:
            start_time = time.time()
            sorted_array = quick_sort_desc(generated_array)
            print(f"Vetor ordenado: {sorted_array}")
            print(f"Tempo de execução: {time.time() - start_time}")
    elif option == 3:
        parse_text_color("Insertion Sort", "1;33")

        if option_sort == 1:
            start_time = time.time()
            sorted_array = Insertion(generated_array)
            print(f"Vetor ordenado: {sorted_array}")
            print(f"Tempo de execução: {time.time() - start_time}")
        else:
            start_time = time.time()
            sorted_array = Insertion_Inverse(generated_array)
            print(f"Vetor ordenado: {sorted_array}")
            print(f"Tempo de execução: {time.time() - start_time}")
    else:
        parse_text_color("Opção inválida", "1;31")
