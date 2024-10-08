import sys

# Đọc dữ liệu đầu vào
def get_input():
    return sys.stdin.read().strip().splitlines()

def process_online_players(input_data):
    active_players = set()  # lưu ID người chơi đang online
    results = []  #  lưu kết quả kiểm tra

    for entry in input_data:
        if entry == '0':
            break
        action, player_id = entry.split()  # Tách hành động và ID người chơi

        if action == '1':  # Đăng nhập
            active_players.add(player_id)
        elif action == '2':  # Kiểm tra online
            results.append('1' if player_id in active_players else '0')
        elif action == '3':  # Đăng xuất
            active_players.discard(player_id)
    
    return results

if __name__ == "__main__":
    input_data = get_input()  # Đọc dữ liệu đầu vào
    output = process_online_players(input_data)  # Gọi hàm xử lý
    print('\n'.join(output))  # In kết quả
