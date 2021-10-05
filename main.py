import random
import time

execution = True

while execution:
    print("""
    Escolha um algoritmo:
    1 - Radix Sort
    2 - Insertion Sort
    3 - Quick Sort
    """)

    option = int(input("Digite a opção desejada: "))

    print("1 - Crescente\n2 - Decrescente\n3 - Aleatório")
    ordenation_type = int(input("Digite o tipo de ordenação: "))

    list_size = int(input("Digite o tamanho da lista: "))

    generate_list = [i for i in range(
        1, list_size + 1) if ordenation_type == 1]
    generate_list_decreasing = [i for i in range(
        list_size, 0, -1) if ordenation_type == 2]
    generate_list_random = [random.randint(
        1, list_size) for i in range(list_size)]

    selected_list = []

    if ordenation_type == 1:
        selected_list = generate_list
    elif ordenation_type == 2:
        selected_list = generate_list_decreasing
    elif ordenation_type == 3:
        selected_list = generate_list_random

    if option == 1:
        from src.radix_sort import radix_sort
        radix_sort()

    elif option == 2:
        from src.insertion_sort import insertion_sort
        insertion_sort()

    elif option == 3:
        from src.quick_sort import quick_sort_desc
        start = time.time()
        quick_sort_desc(selected_list)
        end = time.time()

        print(f"Tempo de execução: {end - start}")
