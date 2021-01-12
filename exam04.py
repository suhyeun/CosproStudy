# 기출문제 풀어보기 04
def func_a(arr):
    counter = [0 for _ in range (1001)]
    for x in  arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret<x:
            ret = x
    return ret

def func_c(arr):
    ret = 1001
    for x in arr:
        if x !=0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

a = [1,2,2,3,1,2,3,1,3,2,1,3,2,2,1]
p =solution(a)
print(p)