# Lessons 1 - Python Basics Done ( 30/12/2022 - 23:54 - Friday )
    # 3 DATA TYPES ( Float , Integer , String )
    # Input AND Print Function



# This program says hello and asks for my name.

#print('Hello,world!')
#print('What is your name?')  # ask for their name
#myName = input('Enter your name: ')
#print('It is nice to meet u, ' + myName)
#print('Your name length is: ')
#print(len(myName))
#print('What is your age?') # ask for their age
#myAge = input('Enter your age: ')
#print('You will be ' + str(int(myAge) + 1) + ' in a year.')




# Lessons 2 - Flow Control Done ( 31/12/2022 - 11:43 - Saturday )
    # Operating with their meaning ( ==, !=, >, <, >=, <= )
    # Binary Boolean Operators ( True/False with 'and' 'or' 'not' )
    # If, else, elif(else if)
    # While Loop & For Loop
    # Import Module ( Random, Sys, Os, Math )



# LogIn Page 

#name = ''
#Input_times = 0
#print('Hi, its nice to meet you . Please enter your username . ')
#name = input("Enter Username Here: ")

#if name == 'YongQIN':
    #print('Hello, ' + name )
    #print('Please enter your password')
    #while Input_times < 5:
        #password = input("Enter Password: ")
        #if password != 'yongqin123':
            #print('Wrong Password, Please try again !')
            #Input_times += 1
        #else:
            #print('Log In Succesfull! Welcome Back, ' + name )
            #break
    #if Input_times >= 5:
        #print('U have input 5 times with false password, please try again later.') 
    
#else:
    #print('New User? Please Sign Up for more ! ')



# This program Require user bark likke a dogg~

#while True:
    #print('Please learn dog bark ')
    #name = input()
    #if name == 'wogh':
        #break
#print('Thank You! Good Dog')




# This program calculate how many week does one year have

#week = []
#for i in range(1,365,7):
    #week.append(i)
    #print('Total weeks for one year is: ' + str(len(week)))



# ROCK, PAPER, SCISSORS 

##import random, sys
##
### These variables keep track of the number of wins, losses, and ties.
##print('ROCK, PAPER, SCISSORS')
##wins = 0
##losses = 0
##ties = 0
##
##while True:  # The main game loop.
##    print(('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)))
##    while True: #The player input loop.
##        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
##        playerMove = input()
##        if playerMove == 'q':
##            print('See u next time.')
##            sys.exit()   # Quit the program.
##        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
##            break  # Break out of the player input loop.
##            print('Type one of r, p, s, or q.')
##         
##
##    # Display what the player chose:
##    if playerMove == 'r':
##        print('ROCK versus...')
##    elif playerMove == 'p':
##        print('PAPER versus...')
##    elif playerMove == 's':
##        print('SCISSORS versus...')
##
##    # Display what the computer chose:
##    randomNumber = random.randint(1, 3)
##    if randomNumber == 1:
##        computerMove = 'r'
##        print('ROCK')
##    elif randomNumber == 2:
##        computerMove = 'p'
##        print('PAPER')
##    elif randomNumber == 3:
##        computerMove = 's'
##        print('SCISSORS')
##
##    # Display and record the win/loss/tie:
##    if playerMove == computerMove:
##        print('It is a tie!')
##        ties = ties + 1
##    elif playerMove == 'r' and computerMove == 's':
##        print('You win!')
##        wins = wins + 1
##    elif playerMove == 'p' and computerMove == 'r':
##        print('You win!')
##        wins = wins + 1
##    elif playerMove == 's' and computerMove == 'p':
##        print('You win!')
##        wins = wins + 1
##    elif playerMove == 'r' and computerMove == 'p':
##        print('You lose!')
##        losses = losses + 1
##    elif playerMove == 'p' and computerMove == 's':
##        print('You lose!')
##        losses = losses + 1
##    elif playerMove == 's' and computerMove == 'r':
##        print('You lose!')
##        losses = losses + 1




# Lessons 3 - Function Done ( 3/1/2023 - 08:39 - Tuesday )
    # Define Function & Call Function Stacks
    # Global statement
    # FUNCTIONS AS “BLACK BOXES”
    # Try & Except




## Call Function Stacks
##
##def a():
##    print('a()starts')
##    b()
##    d()
##    print('a() returns')
##
##def b():
##    print('b() starts')
##    c()
##    print('b() returns')
##
##def c():
##    print('c() starts')
##    print('c() returns')
##
##def d():
##    print('d() starts')
##    print('d() returns')
##a()



# The variable inside function cannot print by outside block.

##def not_work():
##    nope = 'this cannot be work.'
##not_work()
##print(nope)


# Instead you can print the variable outside block.

##def is_work():
##    print(call)
##call = 'i want to go out'
##is_work()



# Take a guess, the order it print.

##def spam():
##    eggs = 'spam local'
##    print(eggs)    
##
##def bacon():
##    eggs = 'bacon local'
##    print(eggs)    
##    spam()
##    print(eggs)    
##
##eggs = 'global'
##bacon()
##print(eggs)        



# Global Function can initial the variable outside block and redefine a new variable inside block.

##def spam():
##  global eggs
##  eggs = 'spam'
##
##eggs = 'global'
##spam()
##print(eggs)
## --------------------------------------
##x = 'i go'
##def globalfun():
##    global x
##    x = 'I back'
##    print('I am global, ' + x)
##globalfun()



# Try & Except

##def spam(divideBy):
##        return 42 / divideBy
##try:
##    print(spam(2))
##    print(spam(12))
##    print(spam(0))
##    print(spam(1))
##except ZeroDivisionError:
##    print("Number 42 can't divide by zero")




# Lessons 4 - Lists ( 3/1/2023 - 08:39 - Tuesday )
    # Getting lists with Index & Slice
    # List Concatenation and List Replication
    # The in and not in Operators
    # The Multiple Assignment Trick
    # Identity and the id() Function




# Index == spam[2]
# Slice == spam[1:4]



# List can use operator +, -, *

##list = [1, 2, 3] + ['A', 'B', 'C']
##print(list)
##
##list = ['X', 'Y', 'Z'] * 3
##print(list)
##
##spam = [1, 2, 3]
##spam = spam + ['A', 'B', 'C']
##print(spam)



# The in and not in Operators

##qna = 'pen' in ['pen','paper','computer','mouse','laptop']
##print(qna)
##qna2 = 'cat' in ['pen','paper','computer','mouse','laptop']
##print(qna2)



##myPets = ['Zeus','Nahida','Paimon']
##print('Enter a pet name: ')
##name = input()
##if name not in myPets:
##    print('I do not have a pet named ' + name)
##else:
##    print(name + ' is my pet.')



# The Multiple Assignment Trick

##cat = ['fat', 'gray', 'loud']
##size = cat[0]
##color = cat[1]
##disposition = cat[2]
##
##print(size)
##print(color)
##print(disposition)

# OR type like this below (faster)

##cat = ['fat', 'gray', 'loud']
##size, color, disposition = cat
##
##print(size)
##print(color)
##print(disposition)



# Random.choice with Lists

##import random
##
##pets = ['Dog', 'Cat', 'Moose','Horse','Cow','Tiger','Rabbit','Dragon','Snake']
##unknown = random.choice(pets)
##print(unknown)



##print('Four score and seven ' + \
##      'years ago...')



# Identity and the id() Function

##identity = id('Miharja')
##print(identity)


##import pprint
##
##message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
##count = {}
##
##for character in message:
##    count.setdefault(character,0)
##    count[character] = count[character] + 1
##
##pprint.pprint(count)




