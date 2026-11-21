sentence=input("enter sentence")
sentence=sentence.split()
i=0
l=""
while len(sentence)>i:
    l+=sentence[i][0].upper()
    i+=1
print(l)