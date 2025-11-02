class Solution(object):
    def indexer(self,l,tar):
        for i in range(len(l)):
            if l[i] == tar:
                return i
        return -1 
    def twoSum(self, nums, target):
        pair=[]
        for i in range(len(nums)):
            search=target-nums[i]
            if search in nums[i+1:]:
                wanted = self.indexer(nums[i+1:], search) + (i+1)
                pair.append(i)
                pair.append(wanted)
                break
        return pair
