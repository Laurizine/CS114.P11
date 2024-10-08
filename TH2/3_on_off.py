# Nguồn tham khảo: ChatGPT

import sys

def main():
    online_players = set()  
    input_data = sys.stdin.read()  
    lines = input_data.strip().splitlines()  

    for line in lines:
        if line == "0":
            break  
        
        action, player_id = map(int, line.split())

        if action == 1:  # đăng nhập
            online_players.add(player_id)
        elif action == 2:  #  online
            print(1 if player_id in online_players else 0)
        elif action == 3:  # đăng xuất
            online_players.discard(player_id)  

if __name__ == "__main__":
    main()

# Dùng lệnh: Get-Content test3.txt | python 3_on_off.py để chạy file input bằng terminal
