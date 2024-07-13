class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''
        roman = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        while num >= 1000:
            answer+=roman[1000]
            num-=1000
        while num >= 100:
            if num//100 == 9:
                answer+=roman[100]+roman[1000]
                num-=900
            elif num//100 == 4:
                answer+=roman[100]+roman[500]
                num-=400
            elif num >= 500:
                answer+=roman[500]
                num-=500
            else:
                answer+=roman[100]
                num-=100
        while num >= 10:
            if num//10 == 9:
                answer+=roman[10]+roman[100]
                num-=90
            elif num//10 == 4:
                answer+=roman[10]+roman[50]
                num-=40
            elif num >= 50:
                answer+=roman[50]
                num-=50
            else:
                answer+=roman[10]
                num-=10
        while num >= 1:
            if num//1 == 9:
                answer+=roman[1]+roman[10]
                num-=9
            elif num//1 == 4:
                answer+=roman[1]+roman[5]
                num-=4
            elif num >= 5:
                answer+=roman[5]
                num-=5
            else:
                answer+=roman[1]
                num-=1
        return answer