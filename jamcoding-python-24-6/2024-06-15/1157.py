word = input()
counter = {}

for char in word:
  if char not in counter:
    counter[char] = 0
  counter[char] = counter[char] + 1

print(counter)
