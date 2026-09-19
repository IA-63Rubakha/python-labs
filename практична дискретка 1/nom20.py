def merge_sorted(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
def merge_into_first(a, b):
    for x in b:
        a.append(x)
    a.sort()
    return a
a1 = [1, 3, 5, 7]
b1 = [2, 4, 6, 8]
print("Злиття:", merge_sorted(a1, b1))
a2 = [1, 3, 5, 7]
b2 = [2, 4, 6, 8]
print("У перший масив:", merge_into_first(a2, b2))