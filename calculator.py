import math
print("operations are :")
print("1 - Add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")
print("5 - power")
print("6 - square root")

result=0

select = int(input("\nselect the opertion :"))
if(select==1):
    num1=float(input("enter the  first value : "))
    num2=float(input("enter the second value : "))
    result=num1+num2
elif(select==2):
    num1=float(input("enter the  first value : "))
    num2=float(input("enter the second value : "))
    result=num1-num2
elif(select==3):
    num1=float(input("enter the  first value : "))
    num2=float(input("enter the second value : "))
    result=num1*num2
elif(select==4):
    num1=float(input("enter the  first value : "))
    num2=float(input("enter the second value : "))
    result=num1/num2
elif(select==5):
    num1=float(input("enter the  first value : "))
    num2=float(input("enter the second value : "))
    result= math.pow(num1,num2)
elif(select==6):
    num=float(input("enter the value :  "))
    result=math.sqrt(num)
else:
    print("enter the valid operation")
    
print("Answer of this operation is ",result)    

