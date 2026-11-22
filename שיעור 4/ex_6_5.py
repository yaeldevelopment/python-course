sentence="the cat saw the dog and the cat ran"
arr=sentence.strip().split()
arr_word=[]
arr_count=[]

for word in arr:
 if word in arr_word:
  index=arr_word.index(word)
  arr_count[index]+=1
 else:
  arr_word.append(word)
  arr_count.append(1)
print(arr_word)
print(arr_count)
#in בודק אם המצא ברשימה רשימה לא חייב להדגיר גודל
   

