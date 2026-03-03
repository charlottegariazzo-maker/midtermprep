a = 2
b = 3
c = "abc"

print(a, b, c)
print(a, b, c, sep=",")

a += 2
a == 5
print(a)

print(c*(a-b))

d = c.find("b")
print(d)

print(d and b)
print(d == True)

e = str(a) + str(b) + str(c) + str(d)
print(e)

print(e[1::2])

print(e + e[::-1])

edit