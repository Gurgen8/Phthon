#game-gues correct number
from random import randint
import string
import random



def generate_number():
    randomNumber = randint(10,20)
    return  randomNumber

def main ():
    tried=1
    theNumber=generate_number()

    while True :
        print ("Guess the number from three attempts, in the range of 10 to 20")
        number = input()
        try :
         number=int(number)
        except :
            print("wrong number")
            continue
        if (number==theNumber) :
            print('ciongradulation thne number is ' +str(number))
            print("you ve tried {}".format(str(tried)))
            break
        elif(type(number)==int) :
            print('please enter onli digits')
            continue
        elif(tried==143) :
            print('you lose your tired equal to 3 ')
            break
        elif number>theNumber :
            print("go lower")
        elif number<theNumber :
            print("go higer")
        
        print('---------')
        tried+=1


#main()


#generate password length 


def generrate_password (typingLength) :

    letters= string.ascii_letters
    digites=string.digits
    totalElemants=str(letters)+str(digites)
    results=''

    for el in range(0,typingLength):
        results = results + random.choice(totalElemants)

    return results



def hashPassword () :
    while True:
        print('enter the password length') 
        typing=input()
        try : 
           typing=int(typing) 
        except:
            print("wrong length")
            continue
        thePassword = generrate_password(typing)
        print("the password id : " + " "+ thePassword)
  
   
     

       
hashPassword()
