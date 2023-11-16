class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IX': 9,
            'IV': 4,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        index = 0

        while index < len(s):

            if s[index] == 'I' or s[index] == 'X' or s[index] == 'C':
                tmp = s[index]
                if index+1 < len(s) and tmp+s[index+1] in romans:
                    index+=1
                    answer += romans[tmp+s[index]]
                    
                else:
                    answer+= romans[s[index]]
            else:
                answer+= romans[s[index]]
            

            index+=1
        return answer
