import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counters = [0] * len(string.ascii_lowercase)
        for pos in range(0, len(s)):
            #print(f'{pos=}')
            #print(f'{s[pos]=}')
            #print(f'{ord(s[pos])=}')
            counters[ord(s[pos]) - ord('a')] += 1
            counters[ord(t[pos]) - ord('a')] -= 1

        return all(x == 0 for x in counters)


        


        





        
        

        


        