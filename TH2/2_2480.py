def truot(hang):
    # Gom cac o so lai, bo qua so 0
    hang_moi = [so for so in hang if so != 0]
    ket_qua = []
    i = 0

    # Gop cac o co cung gia tri
    while i < len(hang_moi):
        if i + 1 < len(hang_moi) and hang_moi[i] == hang_moi[i + 1]:
            ket_qua.append(hang_moi[i] * 2)
            i += 2  # Bo qua o da gop
        else:
            ket_qua.append(hang_moi[i])
            i += 1

    # Dien them cac o trong
    return ket_qua + [0] * (len(hang) - len(ket_qua))

def chuyen_doi(bang):
    return [list(hang) for hang in zip(*bang)]

def truot_len(bang):
    # Truot tung cot len tren (su dung chuyen_doi)
    bang_chuyen = chuyen_doi(bang)
    bang_moi = [truot(hang) for hang in bang_chuyen]
    return chuyen_doi(bang_moi)

def truot_xuong(bang):
    # Truot tung cot xuong duoi
    bang_chuyen = chuyen_doi(bang)
    bang_moi = [truot(hang[::-1])[::-1] for hang in bang_chuyen]
    return chuyen_doi(bang_moi)

def truot_trai(bang):
    return [truot(hang) for hang in bang]

def truot_phai(bang):
    return [truot(hang[::-1])[::-1] for hang in bang]

def main():
    # Nhap vao bang 4x4
    bang = [list(map(int, input().split())) for _ in range(4)]

    # Nhap vao huong di chuyen
    di_chuyen = input().strip()

    # Xu ly theo huong di chuyen
    if di_chuyen == 'L':
        bang = truot_trai(bang)
    elif di_chuyen == 'R':
        bang = truot_phai(bang)
    elif di_chuyen == 'U':
        bang = truot_len(bang)
    elif di_chuyen == 'D':
        bang = truot_xuong(bang)

    # Xuat trang thai cua bang sau khi di chuyen
    for hang in bang:
        print(" ".join(map(str, hang)))

if __name__ == "__main__":
    main()
