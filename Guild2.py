n = int(input())
data = list(map(int,input().split()))
data.sort() # 오름차순으로 정렬 

result = 0 # 총 그룹의 수 
count = 0 # 현재 그룹에 포함된 멤버 수 

for i in data: # 모험가의 공포도 확인 낮은 것 부터 
  count+=1
  if count >= i: # 멤버 수 >= 공포도 라면 
    result += 1 # 그룹 결성 
    count = 0

print(result)
    
