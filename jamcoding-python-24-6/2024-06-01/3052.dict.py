values = {}

for _i in range(10):
  a = int(input())
  b = 42
  c = a % b
  if c in values:
    values[c] = values[c] + 1
  else:
    values[c] = 1

print(len(values))

