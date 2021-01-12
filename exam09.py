# 기출문제 따라하기 09
def solution(characters):
    result = ""
    result += characters[0]
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result += characters[i]
    return result

characters = "seeeeeeeennnnteeeeenccccccccccce"
ret = solution(characters)
print(ret)