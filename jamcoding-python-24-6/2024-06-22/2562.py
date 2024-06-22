result, x = -1, -1
for i in range(9):
  n = int(input())
  if n > result:
    result = n
    x = i

print(result)
print(x + 1)
