class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        jewel = set()
        for je in jewels:
            jewel.add(je)

        for st in stones:
            if st in jewel:
                answer+=1
        return answer