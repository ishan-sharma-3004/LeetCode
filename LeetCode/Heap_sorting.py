import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap=[]
        final=[]
        for i in range(len(nums)):
            heapq.heappush(heap,nums[i])
        while(heap):
            a=heapq.heappop(heap)
            final.append(a)

        return final