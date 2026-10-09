class Solution(object):
  def twosum(self,nums,target):
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
          return [i,j]
s=Solution()
print(s.twosum([7,3,2],5))



# seen={}
#         for i in range(len(nums)):
#             required=target-nums[i]
#             if required in seen:
#                 return [seen[required],i]
#             seen[nums[i]]=i