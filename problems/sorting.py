# selection sort
def selection_sort(arr):
    for i, v in enumerate(arr):                     # O(n)
        for j in range((i + 1), len(arr)):          # O(n)
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j != 0:
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

            j -= j

    return arr


def bubble_sort():
    pass


def merge_sort(arr):
    arr_len = len(arr)
    arr_mid_index = arr_len // 2

    L = arr[:arr_mid_index]
    R = arr[arr_mid_index:]

    merge_sort(L)
    merge_sort(R)

    return arr


# testing

ARR = [64, -34, 25, 12, 22, 11, 90]

print(selection_sort(ARR))
print(insertion_sort(ARR))

ARR2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ARR2[0:11:2])
