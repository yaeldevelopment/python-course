#א
a = 5
b = a
a = a + 2
b = b * a
print(a, b)
# a b
# 5 5
# 7 5
# 7 35

#ב
x = "5"
y = 3
print(x * y, int(x) * y)
# x   y
# "5" 3
# "555" 15
#ג #
count = 0
count += 1
count *= 10
count -= 3
print(count)
# count
# 0
# 1
# 10
# 7
#ד
loss = 1.0
loss /= 4
loss **= 2
print(loss)
# loss
# 1.0
# 0.25
# 0.0625 0.25^2