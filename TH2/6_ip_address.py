def restore_ip_addresses(s: str):
    def is_valid(segment):
        # Kiểm tra xem phần segment có hợp lệ hay không
        if len(segment) > 1 and segment[0] == '0':  # Không được phép có số 0 đứng đầu
            return False
        if 0 <= int(segment) <= 255:
            return True
        return False

    def backtrack(start=0, parts=[]):
        # Nếu đã có đủ 4 phần và đã duyệt hết chuỗi, ta có một IP hợp lệ
        if len(parts) == 4:
            if start == len(s):
                result.append('.'.join(parts))
            return
        
        # Thử tạo phần tiếp theo dài từ 1 đến 3 ký tự
        for length in range(1, 4):
            if start + length <= len(s):
                segment = s[start:start + length]
                if is_valid(segment):
                    backtrack(start + length, parts + [segment])

    result = []
    backtrack()
    return result

# Nhập chuỗi đầu vào từ người dùng
s = input()

# Gọi hàm và in kết quả
result = restore_ip_addresses(s)
for ip in result:
    print(ip)
