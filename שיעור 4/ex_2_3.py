#א
# val,min,max=input("enter value, min and max: ").split(",")
# val = int(val)
# min = int(min)
# max = int(max)
# print("the value is:",(val-min)/(max-min) )
#ב
time=input("enter time in seconds: ")
time=int(time)
h=time//(60*60)
m=time%(h*60*60)//60
s=time%(h*60*60)%(m*60)
print("the time is:",h,":",m,":",s)


