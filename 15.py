class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        l=len(nums)
        sum=0
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            x = nums[i]
            start = i+1
            end = l-1
            while start < end:
                total = x + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    triplets.append([x, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
        return triplets
