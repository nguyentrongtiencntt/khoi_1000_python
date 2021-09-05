# Tính S(n) = x + x^2/2! + x^3/3! + … + x^n/N!
n = 6
s = 0
x = 2
for i in range(1, n):
    s = s + pow(x, i) / i

print("sum of x + x^2/2! + x^3/3! + … + x^n/N! = " + str(s))
