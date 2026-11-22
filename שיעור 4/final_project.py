positive = ["good", "great", "love", "excellent", "happy"]
negative = ["bad", "terrible", "hate", "awful", "sad"]
sentence=input("enter sentence:")


num_positive=0
num_negative=0
for char in ".,!":
    sentence = sentence.replace(char, "")
words=sentence.split()
for i in range(len(words)):
   word = words[i]
   if word in positive:
    if i>0 and word[i-1].lower()=="not":
       num_negative+=1
    else:
       num_positive+=1
   elif word in negative:
      if i>0 and word[i-1].lower()=="not":
            num_positive+=1
      else:
            num_negative+=1
score = num_positive - num_negative


print("positive" if score > 0
      else "negative" if score < 0
      else "neutral")      
 
   
  
       
       

