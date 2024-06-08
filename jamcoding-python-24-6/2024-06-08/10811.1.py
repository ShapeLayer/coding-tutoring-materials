# https://boj.kr/10811

# 입력 받아오기
n, m = input().split()
n = int(n)
m = int(m)

## N을 이용해서 1~N을 담는 리스트 만들기
arr = []
for i in range(n):
  arr.append(i + 1)

# 역순으로 돌리기
## m회 반복
for _i in range(m):
  i, j = input().split()
  i = int(i) - 1
  j = int(j) - 1

  arr[i:j + 1] = arr[i:j + 1][::-1]

# 출력하기

print(*arr)
