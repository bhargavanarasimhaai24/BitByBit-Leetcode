class Solution(object):
    def distinctDifferenceArray(self, nums):
        result=[]
        for i in range(len(nums)):
            part1=nums[0:i+1]
            part2=nums[i+1:]
            dpart1=[]
            dpart2=[]
            for i in part1:
                if i not in dpart1:
                    dpart1.append(i)
            for i in part2:
                if i not in dpart2:
                    dpart2.append(i)
            result.append(len(dpart1)-len(dpart2))
        return result
