# https://boj.kr/10871
n, x = map(int, input().split())
a = [*map(int, input().split())]

b = []

for i in range(n):
  now = a[i]
  if now < x:
    b.append(now)

print(*b)
