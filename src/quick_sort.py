# O algoritmo Quick Sort é um dos mais eficientes para ordenar listas.
# Ele utiliza o pivô como ponto de partição, e divide a lista em duas sublistas
# de elementos menores e maiores do que o pivô.
# Também é recursivo, e a cada chamada ele divide a lista em duas sublistas
# de tamanho 1, e a partir das sublistas, ele chama-se novamente o algoritmo.

# Ordenação em ordem crescente

def quick_sort(arr, swap_times=0):
    # Se a lista tiver tamanho 1, retorna a mesma lista
    if len(arr) <= 1:
        return arr
    else:
        # Pivô é o primeiro elemento da lista
        pivot = arr[0]
        # Separa a lista em duas sublistas, uma com elementos maiores que o pivô
        left = [x for x in arr[1:] if x <= pivot]
        # outra com elementos menores que o pivô
        right = [x for x in arr[1:] if x > pivot]
        # Soma a quantidade de trocas da sublista esquerda com a sublista direita
        swap_times += len(left) + len(right)
        # Chama o algoritmo recursivamente para as sublistas
        return quick_sort(left) + [pivot] + quick_sort(right)
