import random
def RandomArray(N):
    result = []
    while len(result) < N:
        num = random.randint(1, N)
        if result.count(num) == 0:
            result.append(num)
    return result
print(RandomArray(5))
print(RandomArray(10))