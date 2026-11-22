n = int(input("Enter N: "))

sum_all = 0
sum_even = 0
sum_squares = 0

for i in range(1, n + 1):
    sum_all += i

    if i % 2 == 0:
        sum_even += i

    sum_squares += i ** 2

print(sum_all)
print(sum_even)
print(sum_squares)


# מציאת N הקטן ביותר שעצרת שלו גדולה ממיליון
factorial = 1
n = 1

while factorial <= 1000000:
    factorial *= n
    if factorial <= 1000000:
        n += 1

print(n)