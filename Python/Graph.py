print("Enter the Number of vertices")
v = int(input())
arr = []
print(arr)
for i in range(0, v):
    temp = []
    for j in range(0, v):
        if(i!=j):
            print("Enter 1 if there exits a edge between", i , "and", j, "else enter 0")
            ans = int(input())
            if( ans == 1):
                temp.append(j)

    arr.append(temp)

print(arr)
