#write a program that checks if a number input by a user is a prime number using for loop
n=int(input("enter the number"))

for i in range(2,n+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break;
    if flag==0:
        print(i,end=" ")
