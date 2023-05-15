class Solution:
    def isHappy(self, n: int) -> bool:

        _set = set()
        while n != 1:
            _set.add(n)
            arr = list(map(int, str(n)))
            for i in range(len(arr)):
                arr[i] = arr[i]**2
            n = sum(arr)
            if n in _set:
                return False
        return True
