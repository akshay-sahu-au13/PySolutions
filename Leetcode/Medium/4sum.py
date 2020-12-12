'''
    Q. Given an array nums of n integers and an integer target, are there elements a, b, c,
    and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array
    which gives the sum of target.
    Notice that the solution set must not contain duplicate quadruplets.
'''


def fourSum(nums, target):
    if len(nums)<4:
        return []
    two_sum_matrix = [ [ 0 for _ in range(len(nums))] for _ in range(len(nums))]
    two_sum_dict = dict()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            two_sum = nums[i]+nums[j]
            two_sum_list = two_sum_dict.get(two_sum,[])
            two_sum_list.append((i,j))
            two_sum_dict[two_sum] = two_sum_list 
            two_sum_matrix[i][j] = two_sum
    ret_set = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            need_num = target - two_sum_matrix[i][j]
            if need_num in two_sum_dict:
                for _i, _j in two_sum_dict.get(need_num):
                    if len(set([i,j,_i,_j]))==4:
                        ret_set.add(tuple(sorted([nums[i], nums[j], nums[_i], nums[_j]])))
    ret_list = [list(t) for t in list(ret_set)]
    return ret_list

if __name__ == "__main__":
    nums = list(map(int,input("Enter the elements of nums sepeareted by comma: ").strip().split(",")))
    target = int(input("Enter the target value: "))
    ans = fourSum(nums, target)
    print(ans)
