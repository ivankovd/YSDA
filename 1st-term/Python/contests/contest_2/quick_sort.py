def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        if not left <= mid <= right:
            return

        quick_sort(array, left, mid)
        quick_sort(array, mid + 1, right)


def partition(array, left, right):
    pivot = array[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    return j


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    quick_sort(array, 0, n - 1)
    print(' '.join(list(map(str, array))))
