sum=1000
ribit=5
year=0
while sum<2000:
    sum=sum * (1 + ribit / 100)
    year+=1
print(round(sum))
print(year)
