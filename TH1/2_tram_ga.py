
row1 = input().strip()  
row2 = input().strip() 

if row1 == "##" and row2 == "##":
    print("Yes")
    exit()

if (row1[0] == "#" and row1[1] == "#") or \
   (row1[0] == "#" and row2[0] == "#") or \
   (row1[1] == "#" and row2[1] == "#") or \
   (row2[0] == "#" and row2[1] == "#"):
    print("Yes")
else:
    print("No")
