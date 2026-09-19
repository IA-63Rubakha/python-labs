x = int(input("Введіть х (1-8):"))
y = int(input("Введіть y (1-8):"))
is_white = ((x + y) % 2 !=0 )
print(" Поле біле:", is_white)