#pattern printing
print("pattern printing")
num=int(input("enter the number of rows you want :"))
bool=input("1 for ascending 0 for descending")
if bool=="1":
    for i in range(0,num+1,1):
        print("*"*i)
        if num == 4:
            print("invalid input")
            break
else:
    for i in range(num,0,-1):
        print("*"*i)

