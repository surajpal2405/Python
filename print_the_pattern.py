#pattern printing
print("pattern printing")
num=int(input("enter the number of rows you want :"))
bool=input("1 for ascending 0 for descending")
if bool=="1":
    for i in range(1,num+1,1):
        print("*"*i)
else:
    for i in range(num,0,-1):
        print("*"*i)

# for(int i=0;i<=5;i++){
#   print("*"*i);
# }