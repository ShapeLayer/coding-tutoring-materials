
word = input()

dic = {}

for i in range(97, 97 + 26):
    key = chr(i)
    dic[key] = -1

for i in range(len(word)):
    key = word[i]

    if dic[key] == -1:
        dic[key] = i

print(*dic.values())
