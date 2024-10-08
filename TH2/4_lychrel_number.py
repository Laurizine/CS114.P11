import time

def is_palindrome(n: int) -> bool:
    """Kiểm tra nếu một số là palindrome."""
    return str(n) == str(n)[::-1]

def reverse_and_add(n: int) -> int:
    """Đảo ngược chữ số của số và cộng với số ban đầu."""
    reversed_n = int(str(n)[::-1])
    return n + reversed_n

def check_lychrel_candidate(n: int):
    """Thực hiện quá trình reverse-and-add cho đến khi ra palindrome hoặc thỏa mãn điều kiện."""
    iterations = 0
    results = []  # Danh sách để lưu các kết quả của mỗi bước reverse-and-add
    
    while iterations < 10000:
        if is_palindrome(n):
            print("NO")  
            for result in results[1:]:  
                print(result)  
            print(n) 
            return
        
        results.append(n)
        n = reverse_and_add(n)
        iterations += 1
        
        if len(str(n)) >= 15000:  # Dừng nếu số vượt quá 15000 chữ số
            print("YES")
            print(iterations)
            print(n)
            return
    
    # Nếu vượt quá 10000 lần lặp mà chưa thành palindrome
    print("YES")
    print(iterations)
    print(n)

if __name__ == "__main__":
    start_time = time.time()  # Bắt đầu đo thời gian
    number = int(input("Nhập số: "))  
    check_lychrel_candidate(number)
    end_time = time.time()  # Kết thúc đo thời gian
    print(f"Thời gian chạy: {end_time - start_time:.6f} giây")  # In ra thời gian chạy
