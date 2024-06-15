

empty = 0

n, m = input().split()
n = int(n)
m = int(m)

baguni = []
for i in range(n + 1):
  baguni.append(empty)

for _i in range(m):
  i, j, k = input().split()
  i = int(i)
  j = int(j)
  k = int(k)

  for p in range(i, j + 1):
    baguni[p] = k

print(*baguni[1:])
