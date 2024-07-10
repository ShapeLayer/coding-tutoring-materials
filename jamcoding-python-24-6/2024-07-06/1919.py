a, b = input(), input()

ac, bc = [0 for i in range(26)], [0 for i in range(26)]

for char in a:
    ac[ord(char) - ord('a')] += 1
for 문자 in b:
    bc[ord(문자) - ord('a')] += 1

d = [abs(ac[i] - bc[i]) for i in range(26)]
print(d)
print(sum(d))
