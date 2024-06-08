# https://boj.kr/10871
n, x = input().split()
n = int(n)
x = int(x)

a = input().split()
for i in range(n):
  a[i] = int(a[i])

b = []

for i in range(n):
  now = a[i]
  if now < x:
    b.append(now)

p = ''
for i in range(len(b)):
  p += str(b[i]) + ' '
print(p)
