n = int(input())
arr = list(map(int,input().split()))
arr.sort()

team = [[] for _ in range(n+1)] 

i=1
j=0

result = 0 # 팀의 개수 
count = 0 # 반복 횟수 

while True:
  if count>=n:
    break
  count +=1
  team[i].append(arr[j])

  if len(team[i])>=arr[j]:
    result+=1
    i+=1 # 다음 리스트로 
  
  j+=1
    
print(team)
print(result)