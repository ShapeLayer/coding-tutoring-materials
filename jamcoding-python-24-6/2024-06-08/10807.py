# https://boj.kr/10807
n = int(input())
arr = input().split()
for i in range(n):
  arr[i] = int(arr[i])
v = int(input())

count = []
for i in range(201):
  count.append(0)

for i in range(n):
  count[arr[i] + 100] += 1

print(count[v + 100])

