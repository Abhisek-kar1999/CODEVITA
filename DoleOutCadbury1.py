def count(a, b):
    min_side = min(a, b)
    max_side = max(a, b)

    i = (min_side, max_side)
    if i in D:
        return D[i]

    if min_side == 0:
        return 0
    if min_side == 1:
        return a * b

    total = max_side // min_side
    new_side = max_side % min_side

    total = total + count(new_side, min_side)
    D[i] = total
    return total


D = {}
P = int(input())
Q = int(input())
R = int(input())
S = int(input())
ans = 0
for i in range(P, Q + 1):
    for j in range(R, S + 1):
        ans += count(i, j)

print(ans, end='')