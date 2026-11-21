x = 0.0
lr = float(input("Enter learning rate: "))

steps = 0

while abs(2 * (x - 3)) >= 0.001 and steps < 1000:
    x = x - lr * 2 * (x - 3)
    steps += 1

print(steps, round(x, 4))