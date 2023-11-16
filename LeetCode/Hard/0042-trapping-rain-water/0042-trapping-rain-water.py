class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        
        stack = []
        
        for i in range(len(height)):
            
            while stack and height[i] > height[stack[-1]]:
                top_idx = stack.pop()
                
                if not stack:
                    break
                dis = i - stack[-1] -1
                water = min(height[stack[-1]], height[i]) - height[top_idx]
                answer += dis*water

            stack.append(i)
        return answer
            