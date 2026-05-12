class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        count = 0
        for i in strs:
            temp = count
            if sol == []:
                sol.append([i])
                continue
            for x in range(len(sol)):
                if sorted(i) == sorted(sol[x][0]):
                    sol[x].append(i)
                    count += 1
                    break
            if temp == count:
                sol.append([i])
            count += 1
        return sol
                
