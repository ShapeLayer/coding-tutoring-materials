
word = input()

arr = []
for _i in range(26):
    arr.append(-1)

for i in range(len(word)):
    c = word[i]
    p = 0
    if c == 'a':
        p = 0
    elif c == 'b':
        p = 1
    elif c == 'c':
        p = 2
    elif c == 'd':
        p = 3
    elif c == 'e':
        p = 4
    elif c == 'f':
        p = 5
    elif c == 'g':
        p = 6 
    elif c == 'h':
        p = 7
    elif c == 'i':
        p = 8
    elif c == 'j':
        p = 9
    elif c == 'k':
        p = 10
    elif c == 'l':
        p = 11
    elif c == 'm':
        p = 12
    elif c == 'n':
        p = 13
    elif c == 'o':
        p = 14
    elif c == 'p':
        p = 15
    elif c == 'q':
        p = 16
    elif c == 'r':
        p = 17
    elif c == 's':
        p = 18
    elif c == 't':
        p = 19
    elif c == 'u':
        p = 20
    elif c == 'v':
        p = 21
    elif c == 'w':
        p = 22
    elif c == 'x':
        p = 23
    elif c == 'y':
        p = 24
    elif c == 'z':
        p = 25
    if arr[p] == -1:
        arr[p] = i
    else:
        arr[p] = min(arr[p], i)
print(*arr)


