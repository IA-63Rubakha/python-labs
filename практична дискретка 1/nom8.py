A = int(input("Введи А:"))
B = int(input("Введи B:"))
count=0
for i in range(A, B + 1):
    print(i, end=" ")
    count +=1
print()
print("Кількість N=", count)