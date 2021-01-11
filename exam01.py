# 기출문제 따라하기 01
def solution(shirt_size):
    answer = [0,0,0,0,0,0]

    for size in shirt_size:
        if size == "XS":
            answer[0] += 1
        elif size == "S":
            answer[1] += 1
        elif size == "M":
            answer[2] += 1
        elif size == "L":
            answer[3] += 1
        elif size == "XL":
            answer[4] += 1
        elif size == "XXL":
            answer[5] += 1

    return answer


shirt_size = ["XS","S","M","L","XL","XXL"]
solution(shirt_size)
print(solution(shirt_size))