# https://boj.kr/10811

# 입력 받아오기
n, m = input().split()
n = int(n)
m = int(m)

## N을 이용해서 1~N을 담는 리스트 만들기
arr = []
for i in range(n):
  arr.append(i + 1)

print(arr)

# 역순으로 돌리기
## m회 반복
for _i in range(m):
  ## 방법 받기
  i, j = input().split()
  i = int(i) - 1
  j = int(j) - 1
  ## 방법을 기초로 역순으로 돌리기
  _new = []
  #_new는arr의i~j번째 값만을 가지는 조그만 리스트
  for k in range(i, j + 1):
    _new.append(arr[k])
  # _new_rev는 _new를 역순으로 정렬할 것 
  _new_rev = []
  len_new = len(_new)
  for l in range(len_new):
    _new_rev.append(_new[len_new - l - 1])
  for l in range(len_new):
    arr[i + l] = _new_rev[l]

# 출력하기

print(*arr)
