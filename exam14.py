# 기출문제 따라하기 14
def solution(scores):
    grade_counter = [0 for i in range(5)]
    for x in scores:
        if x >= 85:
            grade_counter[0] += 1
        elif x >= 70:
            grade_counter[1] += 1
        elif x >= 55:
            grade_counter[2] += 1
        elif x >= 40:
            grade_counter[3] += 1
        else:
            grade_counter[4] += 1
    return grade_counter

# TEST
scores1 = [100, 98, 45, 33, 74, 22, 65, 78, 59]
ret1 = solution(scores1)
print(ret1)