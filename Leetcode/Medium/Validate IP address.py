## https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        Addr = IP.split(":")
        if len(Addr) == 1:
            Addr = IP.split(".")
        print(Addr)
        if len(Addr) == 4:
            for i in Addr:
                if 1 <= len(i) <= 3 and i.isdigit() and 0 <= int(i) <= 255:
                    if len(i) > 1 and i[0] == "0":
                        return "Neither"
                    else:
                        continue
                else:
                    return "Neither"
                
            return "IPv4"
        
        elif len(Addr) == 8:
            for j in Addr:
                if 1 <= len(j) <= 4:
                    for k in j:
                        if k.isdigit():
                            continue
                            
                        else:
                            if k not in "abcdef" and k not in "ABCDEF":
                                return "Neither"
                            else:
                                continue
                else:
                    return "Neither"
            return "IPv6"
                        
        else:
            return "Neither"