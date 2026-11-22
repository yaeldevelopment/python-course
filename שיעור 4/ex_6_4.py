data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 9, 2, 6, 5, 3]
length=len(data)
cut = int(length * 0.8)
train = data[:cut]
test = data[cut:]
print(train)
print(test)
