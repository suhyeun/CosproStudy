# 기출문제 따라하기 19
def solution(price, money):
    answer = 0
    total = 0

   for i in price:
       total += i
       answer = money - total

       if answer < 0:
           answer = -1
        
    return answer

