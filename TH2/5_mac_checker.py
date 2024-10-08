def kiem_tra_mac(dia_chi_mac):
    nhom = dia_chi_mac.split('-')

    if len(nhom) != 6:
        return False
    
    for phan in nhom:
        if len(phan) != 2:
            return False
        for ky_tu in phan:
            if not (ky_tu.isdigit() or "A" <= ky_tu <= "F"):
                return False
    return True

def nhap_dia_chi_mac():
    danh_sach_mac = []
    while True:
        dia_chi = input().strip()
        if dia_chi == '.':
            break
        danh_sach_mac.append(dia_chi)
    return danh_sach_mac

def main():
    danh_sach_mac = nhap_dia_chi_mac()
    
    for dia_chi in danh_sach_mac:
        print("true" if kiem_tra_mac(dia_chi) else "false")

if __name__ == "__main__":
    main()
