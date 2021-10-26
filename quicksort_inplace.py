# Moves the pivot into place to match the lesser and greater property (compared to the pivot)
# Returns the final index of the pivot's location
def partition(ls, low, high):
    i = low - 1
    pivot = ls[high]
    for j in range(low, high):
        if ls[j] <= pivot:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    ls[i + 1], ls[high] = ls[high], ls[i + 1]
    return i + 1

# A recursive implementation of quicksort that uses in-place swaps rather than object copies
def quicksort_inplace(ls, low=0, high=None):
    if high == None:
        high = len(ls) - 1
    if low < high:
        part_index = partition(ls, low, high)
        quicksort_inplace(ls, low, part_index - 1)
        quicksort_inplace(ls, part_index + 1, high)
