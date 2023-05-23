def selection_sort(arr):
    # algoritmo de ordenamiento por selección
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# lista
arr = [64, 25, 12, 22, 11, 100, 10000, 5, 15, 34]

selection_sort(arr)

print("Lista ordenada:", arr)
