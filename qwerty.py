import random
tuz = 11
valet = 2
korol = 4
dama = 3
z = ["tuz(11)", "valet(2)", "korol(4)", "dama(3)"]
a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 0
while True:
    s = random.sample(a, random.randint(1, 3))
    if len(s) < 3:
        s.extend(random.sample(z, 3 - len(s)))
    print(f"Введите число которое выбрали {s}") 
    m = int(input())
    b += m
    if b == 21:
        print("You winner")
        break
    elif b > 21:
        print(f"You have {b} points and you lose")
        break

        


