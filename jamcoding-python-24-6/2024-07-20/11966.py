n = int(input())

if n == 1:
    print(1)
    exit()

is_even = False
while True:
    if n == 2:
        is_even = True
    else:
        if n % 2 == 1:
            break
        n //= 2

print(int(is_even))

