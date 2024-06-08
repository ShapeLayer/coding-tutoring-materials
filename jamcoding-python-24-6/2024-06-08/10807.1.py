# https://boj.kr/10807
n = int(input())
arr = input().split()
for i in range(n):
  arr[i] = int(arr[i])
v = int(input())

count = 0
for i in range(n):
  if arr[i] == v:
    count += 1

print(count)

