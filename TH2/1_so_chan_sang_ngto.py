def kiem_tra_nguyen_to(n):
    """Kiểm tra xem một số có phải là số nguyên tố không."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dem_cach_phan_tich(s):
    """Đếm số lượng cách phân tích số chẵn thành tổng của hai số nguyên tố."""
    dem = 0
    for a in range(2, s // 2 + 1):
        b = s - a
        if kiem_tra_nguyen_to(a) and kiem_tra_nguyen_to(b):
            dem += 1
    return dem

def main():
    # Nhập số chẵn lớn hơn 2
    so_chan = int(input())
    
    if so_chan <= 2 or so_chan % 2 != 0:
        print()
        return
    
    # Đếm số cách phân tích và xuất kết quả
    so_cach = dem_cach_phan_tich(so_chan)
    print(so_cach)

if __name__ == "__main__":
    main()
