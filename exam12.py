# 기출문제 따라하기 12
def func_a(s):
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret

def solution(scores):
    sum = func_b(scores)
    max_score = func_c(scores)
    min_score = func_a(scores)
    return sum - max_score - min_score

socres1 = [100,90,80,44,77,99,67]
ret1 = solution(socres1)
print(ret1)
