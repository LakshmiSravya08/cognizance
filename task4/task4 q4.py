# palindrome number: It is a symmetrical number which remains the same even when its digits are reversed.
num=int(input("enter any number:-"))
temp=num
nrev=0
while(num>0):
     k=num%10
     nrev=nrev*10+k
     num=num//10
if (temp==nrev):
    print("the given number is a palindrome number!")
else:
    print("the given number is not a palindrome number!")