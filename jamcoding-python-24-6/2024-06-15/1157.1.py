word = input().upper()
counter = {}

for char in word:
  counter[char] = 0

for char in word:
  counter[char] += 1

f = max(counter.values())
f_char = []

for key in counter:
  if counter[key] == f:
    f_char.append(key)

if len(f_char) >= 2:
  print('?')
else:
  print(f_char[0])
