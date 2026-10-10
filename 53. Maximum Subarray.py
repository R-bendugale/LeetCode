class Solution(object):
  def maxsum(self,nums):

    current_sum=nums[0]
    max_sum=nums[0]

    for i in range(1,len(nums)):
      num=nums[i]

      current_sum = max(num,num+current_sum)
      max_sum = max(max_sum,current_sum)
    return max_sum
  
s=Solution()
print(s.maxsum([3,-1,5,-9]))
  