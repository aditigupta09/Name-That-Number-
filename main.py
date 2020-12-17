import random
import pyttsx3

engine = pyttsx3.init()
engine.say("what is your name ?")
engine.runAndWait()
name = input("what is your name ? : ")
print("okay! " + name + " I am guessing a number  between 1 an 10...")
engine.say("okay! " + name + " I am guessing a number  between 1 an 10...")
engine.runAndWait()


n = random.randint(0,10)

'''for _ in range(0,3):
    num = int(input())
    if n in range(0, 5) and num > 6:
        print("your guess is too high")
    elif n in range(0, 5) and num < 6:
        print("your guess is nearby")
    elif n in range(5, 10) and num < 5:
        print("your guess is too low")
    elif n in range(5, 10) and num > 5:
        print("your guess is nearby")
    else:
        print("nice")
'''
for _ in range(0,5):
    guess = int(input())
    if guess < n:
        print("your guess is too low")
        engine.say("your guess is too low")
        engine.runAndWait()
    elif guess > n:
        print("your guess is too high")
        engine.say("your guess is too high")
        engine.runAndWait()
    else:
        print("nice !")
        engine.say("well played !")
        engine.runAndWait()
        break;

if guess == n:
    print("nice !")
    engine.say("well played !")
    engine.runAndWait()
else:
    print()
    print("you did not guess the number right !")
    engine.say("you did not guess the number right !")
    engine.runAndWait()