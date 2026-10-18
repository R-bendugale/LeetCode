nums=[0,1,3,4]
# actual_sum=sum(nums)
# print(actual_sum)
# i=len(nums)
# expected_sum=(i*(i+1))//2
# missing_sum=expected_sum-actual_sum
# print(missing_sum)

# xor
result=0
for i in range(len(nums)+1):
  result^=i
for i in nums:
  result^=i
print(result)
