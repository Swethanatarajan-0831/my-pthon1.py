#fibo
num=int(input("Enter a number:"))
a=-1
b=1
i=1
while(i<=num):
    fibo=a+b
    a=b
    b=fibo
    i+=1
    print(fibo)
