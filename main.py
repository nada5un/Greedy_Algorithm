n,m,k = map(int,input().split())
number_list = list(map(int,input().split()))

m_count = m//k 
o_count = m%k

max_number = max(number_list)
number_list = sorted(number_list,reverse=True)

if number_list[1]==number_list[0]==max_number:
  sum = max_number*n
else:
  sum = max_number*k*m_count + number_list[1]*o_count

print(sum)


