n,m = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

count = 0

for a in arr:
  now = a
  for b in arr:
    print(a,b)
    if b!= now:
      count+=1

print(count//2)