class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def get_counters(line: str):
            counters = dict()
            for i in line:
                counter = counters.get(i)
                if counter == None:
                    counters[i] = 1
                else:
                    counter += 1
                    counters[i] = counter

            return counters

        return get_counters(s) == get_counters(t)




        
        

        


        