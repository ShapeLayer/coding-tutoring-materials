for a in range(1, 101):
    for b in range(1, 100):
        for c in range(b, 100):
            for d in range(c, 100):
                if a ** 3 == (b ** 3 + c ** 3 + d ** 3):
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
                if a ** 3 < (b ** 3 + c ** 3 + d ** 3):
                    break

