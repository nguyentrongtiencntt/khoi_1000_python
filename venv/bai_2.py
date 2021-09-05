# Bài 2: Tính S(n) = 1^2 + 2^2 + … + n^2
n = 6
s = 0
for i in range(1, n):
    s = s + pow(i, 2)

print("sum of 1^2 + 2^2 + … + n^2 = " + str(s))
