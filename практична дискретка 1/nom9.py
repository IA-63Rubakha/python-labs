N = int(input("Введи ціле число N (N > 0): "))
reversed_num = 0
while N > 0:
    digit = N % 10
    reversed_num = reversed_num * 10 + digit
    N = N // 10
print("Число навпаки =", reversed_num)