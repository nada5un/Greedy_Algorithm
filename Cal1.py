# 한줄로 숫자 입력 받기 
arr = list(input())

cal = list()
result = 0
st = ''

for a in arr:
  if a == '0' or a=='1':
    cal.append(a)
    cal.append('+')
  else:
    cal.append(a)
    cal.append('*')

for i in range(len(cal)):
  if cal[i] == '+' or cal[i]=='*':
    temp_i = i
    if temp_i != 1:
      st = str(eval(st))
  st += cal[i]

print(st[:-1])  
