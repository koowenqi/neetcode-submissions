class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pnums = []
        for i in range(len(nums)):
            product = None
            for x in range(len(nums)):
                if i == x:
                    continue
                if product == None:
                    product = nums[x]
                    continue
                product *= nums[x]
            pnums.append(product)
        return pnums