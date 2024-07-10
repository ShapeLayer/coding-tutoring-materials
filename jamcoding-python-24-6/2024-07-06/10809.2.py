
word = input()

arr = []
for _i in range(26):
    arr.append(-1)

for i in range(len(word)):
    c = word[i]
    p = ord(c) - ord('a')

    if arr[p] == -1:
        arr[p] = i

print(*arr)

