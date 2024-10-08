def find_squares(A, B):
    x1, y1 = A
    x2, y2 = B
    AB = (x2 - x1, y2 - y1)
    perp1 = (-AB[1], AB[0])
    perp2 = (AB[1], -AB[0])
    C1 = (x1 + perp1[0], y1 + perp1[1])
    D1 = (x2 + perp1[0], y2 + perp1[1])
    C2 = (x1 + perp2[0], y1 + perp2[1])
    D2 = (x2 + perp2[0], y2 + perp2[1])
    print(f"({x1}, {y1}) ({C1[0]}, {C1[1]}) ({D1[0]}, {D1[1]}) ({x2}, {y2})")
    print(f"({x1}, {y1}) ({x2}, {y2}) ({D2[0]}, {D2[1]}) ({C2[0]}, {C2[1]})")
# Hàm em có tham khảo trên gemini ạ
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
find_squares(A, B)
