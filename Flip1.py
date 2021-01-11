data = list(input())

# 연속된 숫자 개수 찾아야 함 
num = int(data[0])
switch = 0

for i in range(len(data)):
  temp = int(data[i]) #현재의 값 
  if num!=temp:
    num = temp
    switch +=1
  else:
    continue

print(switch-1)

