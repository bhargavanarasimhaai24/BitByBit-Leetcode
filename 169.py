class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for i in nums:
            if i in freq:
                freq[i]=freq.get(i,0)+1
            else:
                freq[i]=1
        major=-1
        for key,val in freq.items():
            if val>len(nums)//2:
                major=key
                break
        return major
