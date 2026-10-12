class Solution():
  def zeros(self,nums):
    j=0
    for i in range(len(nums)):
      if nums[i]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        j+=1
nums=[0,1,3933,0,34]
s=Solution()
s.zeros(nums)
print(nums)