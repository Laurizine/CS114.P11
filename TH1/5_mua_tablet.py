import math as m

def xu_ly(n):
    dem = 0
    can2 = 1 / m.sqrt(2)  
    n2 = n * n 

    for a in range(1, int(n * can2) + 1):
        b2 = n2 - a * a
        b = m.isqrt(b2)  
        if b * b == b2: 
            dem += 1
    return dem

n = int(input())
print(xu_ly(n))
