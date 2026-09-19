def sort_asc(arr):
    return sorted(arr)
def sort_desc(arr):
    return sorted(arr, reverse=True)
test = [5, 2, 9, 1, 7]
print("За зростанням:", sort_asc(test))
print("За спаданням:", sort_desc(test))