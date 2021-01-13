def solution(arr, k):
  answer = 0
  total = 0

  for i in arr:
    total += i

  answer = k - total

  if answer < 0 :
    answer = -1

  return answer

arr1 = [2100, 3200, 2100, 800]
ret1 = solution(arr1, 10000)
print(ret1)