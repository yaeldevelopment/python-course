numbers = [0, 0, 0, 0]
n_numbers=numbers.copy()
min_num=numbers[0]
max_num=numbers[0]
for i in numbers:
    if max_num<i:
        max_num=i
    elif min_num>i:
       min_num=i
if min_num==max_num:
    n_numbers=[0 for i in numbers]
else:
    for i in  range(len(numbers)):
     n_numbers[i]=round((n_numbers[i]-min_num)/(max_num-min_num),2)
print(n_numbers)

