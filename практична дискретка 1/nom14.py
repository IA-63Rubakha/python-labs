for attempt in range(5):
    guess = int(input("Введи число: "))
    if guess == 5:
        print("Молодець! Ти вгадав!")
        break
else:
    print("Спроби закінчилися")