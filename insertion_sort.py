def insertion_sort(values):
    outer_pass = 0
    inner_pass = 0

    for i in range(1, len(values)):
        outer_pass += 1
        j = i
        while j > 0 and values[j] > values[j]:
            inner_pass += 1
            values[j], values[j - 1] = values[j - 1], values[j]
            j -= 1

