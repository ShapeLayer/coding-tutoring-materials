n = int(input())
arr = [*map(int, input().split())]

m = max(arr)
for i in range(n):
    arr[i] = (arr[i] / m) * 100

print(sum(arr) / n)

