class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for num in nums:
            if num in seen:
                return  True
            else:
                seen.add(num)
        return False
s=Solution()
print(s.containsDuplicate([1,2,3,4,1]))