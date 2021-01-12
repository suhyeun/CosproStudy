# 기출문제 따라하기 08
def solution(sentence):
    str = ""
    for c in sentence:
        if c != "." and c != " ":
            str += c
    size = len(str)
    for i in range(size//2):
        if str[i] != str[size-1-i]:
            return False
    return True

sentence1 = "never odd or even"
ret1 = solution(sentence1)

print(ret1)