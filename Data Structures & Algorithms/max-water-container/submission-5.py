class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        ans = -1
        while p1 < p2:
            ans = max(ans, (min(heights[p2],heights[p1]) * (p2-p1)))
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return ans

        