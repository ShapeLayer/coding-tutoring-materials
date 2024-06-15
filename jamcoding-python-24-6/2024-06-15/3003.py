arr = input().split()
for i in range(6):
  arr[i] = int(arr[i])

a, b, c, d, e, f = arr

a = 1 - a
b = 1 - b
c = 2 - c
d = 2 - d
e = 2 - e
f = 8 - f

print(a, b, c, d, e, f)

