## https://leetcode.com/problems/combination-sum/


def combinationSum(candidates, target):
    res = []
    def solve(now, needed):
        if not needed:
            res.append(now)
            return
        for num in candidates:
            if num <= needed and ((not now) or (now and num >= now[-1])):
                solve(now+[num], needed-num)            
    solve([], target)
    return res

if __name__ == '__main__':
    candidates = list(map(int,input().split()))
    target = int(input())
    print(combinationSum(candidates, target))