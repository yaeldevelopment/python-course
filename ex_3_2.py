str=input("enter str")
str=str.strip()#מוחק רווחים מיותרים
str=str.lower()
str=str.replace(",","")#מוחק פסיקים 
str = " ".join(str.split())
count=len(str.split())
print(str)
print(count)