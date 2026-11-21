num=int(input("enter num with four digits: "))
s=num
sum=0
num_revers=0
while num!=0:
    sum+=num%10
    num_revers=num_revers*10+num%10
    num//=10
print("the sum of the digits is:",sum)  
print("the reversed number is:",num_revers)  
print("the is palindrome:",num_revers==s)
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
print(num[::-1])#הופך את המחרוזת
