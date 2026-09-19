list1 = ["яблуко", "банан", "груша", "слива"]
list2 = ["банан", "ківі", "груша", "манго"]
result = []
for word in list1:
    if word not in list2:
        result.append(word)
for word in list2:
    if word not in list1:
        result.append(word)
print(result)