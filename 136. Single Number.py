nums=[1,2,3,2,1,4,3]
# count={}
# for i in nums:
#   if i in count:
#     count[i]+=1
#   else:
#     count[i]=1
# for i in count:
#   if count[i]==1:
#     print(i)

result=0
for i in nums:
  result^=i
print(result)