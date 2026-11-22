secret=int(input("enter the secret: "))
count=0
while secret!=37:
    if(secret>37):
        print("lower")
    else:
        print("higher") 
    count+=1  
    secret=int(input("enter the secret: "))

print(f"it took you {count} guesses")
#7 ניחושים
