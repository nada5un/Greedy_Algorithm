n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

count = 0

for i in range(n):
  now = arr[i]
  for j in range(i+1,n):
    if now!=arr[j]:
      count+=1

print(count)