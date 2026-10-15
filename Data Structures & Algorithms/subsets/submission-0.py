class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []

        subset = []
        def iterate(index):
            if index >= n:
                answer.append(subset.copy())
                return

            subset.append(nums[index])
            iterate(index + 1)
            
            subset.pop()
            iterate(index + 1)
        iterate(0)
        return answer