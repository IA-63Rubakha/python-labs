arr = [10, 25, 7, 40, 15, 30, 5, 50]
total = 0
for x in arr:
    total += x
average = total / len(arr)
print("Середнє =", average)
for i in range(len(arr)):
    if arr[i] > average:
        arr[i] = arr[i] - 18
print("Новий масив =", arr)