import random

while True:
    flag = True
    while flag:
        num = input('Type a number which will be your end digit: ')
        if num.isdigit():
            print("Let's Play!!")  
            num = int(num)
            flag = False
        else:
            print("Invalid Entry! Try Again!")

    Secret = random.randint(1,num)

    guess = None
    count = 1

    while guess != Secret:
        guess = input("please type a number between 1 and " + str(num) + ": ")
        if guess.isdigit():
            guess = int(guess)

        if guess == Secret:
            print('You got it! Congrulation!')
        else:
            print("please try again!")
            count += 1

        if count> 5 :
            print("U lose as it took more then 5 chances. The number was " + str(num))
        

          

            
