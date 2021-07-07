 #faulty calculator of below operations only and regular for other opeations
 # why is this named a faulty calculator anyway ???????????????

#45 *  = 555, 56 + 9 = 77, 56 / 6 = 4
num1=int(input("enter num1"))
op=input("+ / - *")
num2=int(input("enter num2"))
if num1==45 and op=="*" and num2==3:
    print("555")
elif num1==56 and op=="+" and num2==9:
    print("77")
elif num1==56 and op=="/" and num2==6:
    print("4")
elif op=="*":
    print(int(num1) * num2)
elif op=="+":
    print(int(num1+num2))
else:
    print(int(num1/num2))
