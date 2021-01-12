# 기출문제 따라하기 17
def solution(s):
    s_list = list(s)
    n= len(s)
    for i in range(n):
        if s_list[i] == "a":
            s_list[i] = "z"
        elif s_list[i] == "z":
            s_list[i] = "a"
    
    return "".join(s_list) # ㅅ트링으로 만들기 위해 join사용
        