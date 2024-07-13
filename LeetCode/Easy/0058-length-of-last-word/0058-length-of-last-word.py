class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(map(str, s.split(' ')))
        pointer = len(words)-1

        while not words[pointer]:
            pointer-=1
        
        return len(words[pointer])