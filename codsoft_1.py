def calculator(n1,n2,op):
    if op=="+":
       print(n1+n2)
    elif op=="-":
       print(n1-n2)
    elif op=="*":
       print(n1*n2)
    elif op=="/":
       if(n2==0):
         print("invalid number")
       else:
         print(n1/n2)
    elif op=="%":
        if n2==0:
            print("invalid number,divisor cannot be zero")
        print(n1%n2)
    else:
       print("invalid operator")
while True:
    try:  
        n1=float(input("enter the first number"))
        n2=float(input("enter the second number"))
    except ValueError:
        print("invalid number,please try again")
        continue
    op=input("enter your operation,(+,-,/,*,%)")
    calculator(n1,n2,op)
    count=input("do you want to perform another?(yes/no)")
    if count.lower()!="yes":
        print("okay")
        break

    


