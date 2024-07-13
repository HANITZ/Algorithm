class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []

        for today, temperature in enumerate(temperatures, 1):
            
            while stack and stack[-1][0] < temperature:
                pretem, pre = stack.pop()
                answer[pre-1] = today-pre
            
            stack.append((temperature, today))

        return answer