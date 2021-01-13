n = int(input())
arr = list(map(int,input().split()))
arr.sort()

coin = []
result = 0

#재귀..??
for i in range(n):
  if arr[i] not in coin:
    # 원래 있던 거 추가 
    coin.append(arr[i])
  for j in range(i+1,n):
    # 두 개씩 더하기 
    result = arr[i]+arr[j]
    if result not in coin:
      coin.append(result)
    for k in range(j+1,n):
      result+=arr[k]
      if result not in coin:
        coin.append(result)

# 만들지 못하는 최소 동전 
for i in range(1,sum(arr)):
  if i not in coin:
    print(i)
    break
