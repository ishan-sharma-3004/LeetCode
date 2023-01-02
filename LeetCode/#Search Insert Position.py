#Search Insert Position
'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''


def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(float('inf'))
        l=0
        r=len(nums)-1
        while(l<r):
            mid=(l+r)//2
            if(target<=nums[mid]):
                r=mid
            else:l=mid+1
        return l      