n = int(input())
arr = input().split()
for i in range(n):
  arr[i] = int(arr[i])

_min, _max = 1_000_000, -1_000_000

for i in range(n):
  if _min > arr[i]:
    # 지금까지의 최소값보다 지금 바라보고 있는 값이 더 작음
    _min = arr[i]
  if _max < arr[i]:
    # 지금까지의 최댓값보다 지금 바라보고 있는 값이 더 큼
    _max = arr[i]

print(_min, _max)
