#write a program which will take the no. entered by the user as an input checks it with already defined no.(any no.)
#if matched will display "your guess is correct" along with the attempts taken to guess. if guess is more tells
#you to decrement the no. along with no. of attempts left and vice versa
#max no. of attempt is 9. if all attempts get used tells "game over"
#This is just a test, will add a comment and will create a pull request, hope this works 

i=24
g=8
while(True):
    num2 = int(input("enter any number"))
    if g==1:
        print("game over")
        break
    elif num2==i:
        print("you guessed it right")
        print("no. of attempts taken : 1")
        break
    elif num2<i:
        print("your guess is less than actual, try guessing more")
        g=g-1
        print("guesses left :", g)
    elif num2>i:
        print("your guess is more than actual, try guessing less")
        g=g-1
        print("attempts left :",g)










