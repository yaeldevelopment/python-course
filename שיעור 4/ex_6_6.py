points = [1.0, 2.0, 3.0, 8.0, 9.0, 10.0]
labels = ["small", "small", "small", "big", "big", "big"]
num=float(input("enter num:"))
for i in range(len(points)):
    if points[i]>num:
        if i>0:
         if((num-points[i-1])>(points[i]-num)):
           print(labels[i])
         else:
                print(labels[i-1])
        else:
           print(labels[i])
        break