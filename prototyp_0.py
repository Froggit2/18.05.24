a = range(1, 21)
g = set()
f = dict()
for n in range(3, 21):
    for x in a:
        for y in a:
            if n % (x + y) == 0:
                if x != y:
                    g.add(n)
                    f[*g] = x, y
                    print(f)
                    g.pop()
                    f.pop()