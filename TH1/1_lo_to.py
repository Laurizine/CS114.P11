
matrix = []
for _ in range(3):
    row = list(map(int, input().split())) 
    matrix.append(row)                     

N = int(input())                         

drawn_numbers = []
for _ in range(N):
    number = int(input())                  
    drawn_numbers.append(number)           

marked = [[False] * 3 for _ in range(3)]   

for i in range(3):
    for j in range(3):
        if matrix[i][j] in drawn_numbers:  
            marked[i][j] = True            

for i in range(3):
    if marked[i][0] and marked[i][1] and marked[i][2]: 
        print("Yes")                      
        exit()                            

for j in range(3):
    if marked[0][j] and marked[1][j] and marked[2][j]: 
        print("Yes")                       
        exit()                         

if marked[0][0] and marked[1][1] and marked[2][2]:
    print("Yes")                          
    exit()                                 

if marked[0][2] and marked[1][1] and marked[2][0]:
    print("Yes")  
    exit()  

print("No")  
