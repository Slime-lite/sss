import random
ver = 0
while (ver == 0):
    player = int(input("1 - К, 2 - Н, 3 - Б "))
    if (player == 1 or player == 2 or player == 3):
        ver = 1
if player == 1:
    print("Камень")
if player == 2:
    print("Ножнецы")
if player == 3:
    print("Бумага")
comp = random.randint(1, 3)
if comp == 1:
    print("Компьютер выбрал К")
if comp == 2:
    print("Компьютер выбрал Н")
if comp == 3:
    print("Компьютер выбрал Б")
if player == comp:
    win = 0
if player == 1 and comp == 2:
    win = 1
if player == 1 and comp == 3:
    win = 2
if player == 2 and comp == 1:
    win = 2
if player == 2 and comp == 3:
    win = 1
if player == 3 and comp == 1:
    win = 1
if player == 3 and comp == 2:
    win = 2
if win == 0:
    print("Ничея")
if win == 1:
    print("Вы победили")
if win == 2:
    print("Вы проиграли")