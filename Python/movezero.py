nums = [3,2,4,7,8,0,5,]
n = len(nums)
i = 0
for j in range(n):
    if (nums[j] != 0):
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
print(nums)