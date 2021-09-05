# Bài 1: Tính S(n) = 1 + 2 + 3 + … + n
def sum(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
    return s


print("sum is " + str(sum(6)))
