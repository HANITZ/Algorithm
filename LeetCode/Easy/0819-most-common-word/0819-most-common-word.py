class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        max_word = ''
        max_times=0

        for key, value in dic.items():
            if value > max_times:
                max_times = value
                max_word= key
        return max_word
        