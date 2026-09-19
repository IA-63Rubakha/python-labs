N = int(input("Введи ціле число N (N > 1): "))
is_prime = True
for i in range(2, N):
    if N % i == 0:
        is_prime = False
        break
print(is_prime)