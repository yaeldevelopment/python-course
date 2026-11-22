grade=float(input("enter grade: "))
sum=0
count=0
while grade!=-1:
    sum+=grade 
    count+=1
    grade=float(input("enter grade: "))
#לא נכנס ללואה בכלל ולכן לא יספרכשזה -1
if count > 0:
    average = round(sum / count, 2)
    print("the average is:", average,"count of grades:", count)
else:
    print("No grades entered.")
