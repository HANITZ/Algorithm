class Solution:
    def trap(self, height: List[int]) -> int:

        answer = 0
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        
        while l < r:
            l_max, r_max = max(l_max, height[l]), max(r_max, height[r])
            if l_max <= r_max:
                answer += l_max - height[l]
                l+=1
            else:
                answer+= r_max - height[r]
                r-=1
        return answer