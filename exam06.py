# 기출문제 따라하기 05
def solution(number):
    count = 0
    for i in range(1, number+1):
        current = i
        temp = count
        while current != 0:
            if current%10 == 3 or current%10 == 6 or current%10 == 9:
                count += 1
                print("짝", end = ' ')
            current = current//10 # 이 구문이 있는 이유
        if temp == count:
            print(i, end=' ')
        print(" ", end=' ')
    print("")
    return count

result = solution(20)
#print(result)

