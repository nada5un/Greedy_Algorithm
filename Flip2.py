data = input()
count0 =0 # 전부 0으로 바꾸는 경우
count1 =0 # 전부 1로 바꾸는 경우 

#첫번째 원소 
if data[0] =='1':
  count0+=1
else:
  count1+=1

#두번째 원소부터 모든 원소 확인 
for i in range(len(data)-1):
  if data[i] != data[i+1]:
    if data[i+1] =='1':
      count0 +=1
    else:
      count1 +=1

print(min(count0,count1))