val_arr = []
val_set = set()

for _i in range(10):
  a = int(input())
  b = 42
  c = a % b
  val_arr.append(c)
  val_set.add(c)

# print(val_arr, val_set, set(val_arr))
print(len(val_set))

