#Bài 4: Tính S(n) = ½ + ¼ + … + 1/2n
def sum(n):
    s = 0
    for i in range(1, n):
        s = s + 1/(2*i)
        print("i = " + str(i) + " => " + "1/(2*i) =" + str(1/(2*i)))
        print("s = " + str(s))
    return s


print("sum of 1 + ½ + ¼  + … + 1/2n " + " is " + str(sum(6)))
