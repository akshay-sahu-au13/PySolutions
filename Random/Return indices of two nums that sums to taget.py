  
# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use
# the same element twice.
# You can return the answer in any order.

if __name__ == "__main__":
    nums = list(map(int,input("Enter space seperated values for nums: ").split()))
    target = int(input("Enter the target value: "))
    def findpairs(nums,target):
        n = len(nums)
        temp = {}
        for i in range(n):
            if target - nums[i] in temp:
                return [temp[target - nums[i]], i]
            else:
                temp[nums[i]] = i
    
    print(findpairs(nums,target))