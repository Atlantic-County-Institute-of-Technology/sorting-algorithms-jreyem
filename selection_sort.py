
def selection_sort(values):
    outer_pass = 0
    inner_pass = 0

    for i in range(len(values)):
        outer_pass += 1
        min_index = i
        for j in range(i + 1, len(values)):
            inner_pass += 1
            if values[j] < values[min_index]:
                min_index = j

        if min_index != i:
            # Swap the found minimum element with the first element
            values[i], values[min_index] = values[min_index], values[i]

    print(outer_pass)
    print(inner_pass)
