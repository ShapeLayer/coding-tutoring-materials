table = []

for i in range(9):
  row = input().split()
  for j in range(9):
    row[j] = int(row[j])
  table.append(row)

result = -1_000_000
x, y = -1, -1

for i in range(9):
  for j in range(9):
    if result < table[i][j]:
      result = table[i][j]
      x, y = i, j

print(result)
print(x + 1, y + 1)

