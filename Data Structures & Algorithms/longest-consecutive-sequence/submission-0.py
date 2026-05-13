class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for i in nums:
            hashset.add(i)
        largest = 0
        for i in hashset:
            count = 1
            if i-1 not in hashset:
                temp = i
                while temp+1 in hashset:
                    count += 1
                    temp += 1
            if count > largest:
                largest = count
        return largest