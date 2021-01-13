# 음식을 모두 먹는데 소요될 시간 리스트 
food_times = list(map(int,input().split()))
# 방송이 중단될 시간 
k = int(input())
n = len(food_times)

def solution(food_times, k):
  n = len(food_times)
  answer = 0
  if sum(food_times)<=k:
    return -1
  # k초 동안 실행 
  for i in range(k):
    if food_times[i%n]<=0:
      i+=1 # 다음 음식으로 
    food_times[i%n] -=1
    i-=1 # 다시 원래대로 
    # print(food_times)

  answer = i%n
  return answer

answer = solution(food_times,k)

print(answer)