nums=[1,1,1,1,2]
count={}
for i in range(len(nums)):
  if nums[i] in count:
    count[nums[i]]+=1
  else:
    count[nums[i]]=1
for i in count:
  if count[i]>len(nums)/2:
    print(i)