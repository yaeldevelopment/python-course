word=input("enter word: ")
sentence=input("enter sentence: ")  

count=sentence.count(word)
sentence=sentence.replace(word,"[MASK]")
print(sentence)
print("the index of the first occurrence of the word is:",count)

