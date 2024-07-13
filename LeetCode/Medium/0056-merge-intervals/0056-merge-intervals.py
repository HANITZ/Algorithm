class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()
        for interval in intervals:
            if answer and interval[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], interval[1])
            else:
                answer.append(interval) 

        return answer