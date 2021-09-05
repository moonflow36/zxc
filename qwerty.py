import random
v = 2
k = 4
d = 3
t = 11
b = 0
c = 21
n = [2, 3, 4, 5, 6, 7, 8, 9, 10, "v", "k", "d", "t"]
while True:
    b = 0
    print(f"Вам выполо: {random.sample(n,3)}")
    a = int(input("Napishite chislo: "))
    b += a
    if b < 21:
        print(f"Вам выполо: {random.sample(n,3)}")
        a = int(input("Napishite chislo: "))
        b += a
    
    if b == 21:
        break
        
    if b > 21:
        break
        


