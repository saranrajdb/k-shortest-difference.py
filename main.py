arr=list(map(int, input().split()))
k = int(input())
arr.sort()
ans = 999999
for i in range(0, len(arr)-k+1):
    temp = max(arr[i : i+k]) - min(arr[i : i+k])
    if temp < ans :
        ans = temp
print(ans)

"""
i/p: arr= 10 100 300 20 30 991 993 992
     k= 3
o/p: 2
"""