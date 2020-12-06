class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        
        def isValid(ss):
            if len(ss) == 0:
                return False
            elif ss.startswith('0'):
                if len(ss) == 1:
                    return True
                else:
                    return False
            else:
                if int(ss) <= 255:
                    return True
        
        def dfs(address, remaining_string, times):
            if times == 0:
                return
            if times == 1:
                if isValid(remaining_string):
                    ret.append(address + [remaining_string])
                return
                    
            nb_next_digits = 1
            while nb_next_digits <= 3:
                cur_string = remaining_string[:nb_next_digits]
                if isValid(cur_string):
                    dfs(address + [cur_string], remaining_string[nb_next_digits:], times - 1)
                nb_next_digits += 1
                    
        dfs([], s, 4)
        ret = ['.'.join(l) for l in ret]
        return ret
    
    
#     def isvalidIP(self,IP):
#         Ip = IP.split(".")
        
#         for i in Ip:
#             if 0 <= len(i) <= 3 and 0 <= int(i) <= 255:
#                 continue
#             else:
#                 return False
#         return True
    
                