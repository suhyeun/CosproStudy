# 기출문제 따라하기 02
def solution(price, grade):
    if grade == "S":
        answer = int(price*0.95)
    elif grade == "G":
        answer = int(price*0.9)
    elif grade == "V":
        answer == int(price*0.85)
    return answer

price = 100
grade = "S"
solution(300, "G")
print(solution(300, "G"))