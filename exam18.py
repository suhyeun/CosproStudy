# 기출문제 따라하기 18
def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n =="j" or n == "k":
                answer += 1
                continue
    return answer

# TEST
names1 = ["jaims", "kim join", "jokin"]
ret = solution(names1)
print(ret)