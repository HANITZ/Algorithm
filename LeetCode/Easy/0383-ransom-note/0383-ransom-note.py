class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        words = collections.defaultdict(int)

        for char in magazine:
            words[char] += 1
        
        for ransom in ransomNote:
            if not words[ransom]:
                return False
            words[ransom] -= 1
        return True