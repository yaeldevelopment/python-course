b=False
for i in [70 ,30 ,27 ,25 ,21 ,15 ,7]:
    b=False
    num=i
    while num!=0:
      if num%10==7:
       print("Boom",end=",")
       b=True       
      num/=10
    if b:
          continue;
    elif i%3==0 and i%5==0:
            print("FizzBuzz",end=",")
    elif i%3==0:
            print("Fizz",end=",")
    elif i%5==0:
             print("Buzz",end=",")
    else:
           print(i,end=",")


    

     
     