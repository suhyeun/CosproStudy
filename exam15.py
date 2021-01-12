# 기출문제 따라하기 15
def solution(stones):
    cnt = 0 # 점프 카운트
    current = 0 # 스톤 위치
    n = len(stones)
    while(current<n):
        current += stones[current]
        cnt += 1
    return cnt