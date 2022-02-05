'''
This is an small voice controlled Python turtle race game. The movement the game starts, we got to move each turtle with voice command "GO".
Following are the required libraries which are required for the functioning of this program
'''


from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
import playsound
import pyttsx3
import random
import os
import turtle


#Set engine to pyttsx3 which is used for text to speech in Python and sapi5 is Microsoft speech application platform interface

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#build voice system to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#function that will listen for commands
def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('JARVIS is ready.......')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("you said:" +command+ "\n")
    except sr.UnknownValueError:
        print("Your Last command couldn't be heard")
        speak("Your Last command couldn't be heard")
        speak('Please repeat')
        command = mycommand()
    return command


die = [0,1,2,3,4,5,6]


#Create turtles for both the players
window = turtle.Screen()
window.bgcolor('magenta')
window.title('The Turtles Race!')
speak("Jarvis is ready")
speak("Lets play the turtle race")

speak("Player one is green turtle")
player_one = turtle.Turtle()
player_one.shape('turtle')
player_one.color('green')
player_one.pu()
player_one.goto(-200, 100)

#Cloned the player_two tutrle from player_one
speak("Player two is red turtle")
player_two = player_one.clone()
player_two.color('red')
player_two.pu()
player_two.goto(-200, -100)


#create a finish line circle
player_one.goto(300,60)
player_one.pd()
player_one.circle(40)
player_one.pu()
player_one.goto(-200,100)
player_one.pd()
player_two.goto(300,-140)
player_two.pd()
player_two.circle(40)
player_two.pu()
player_two.goto(-200, -100)
player_two.pd()
speak('You need to reach the center of this respective to circle to win the race')


start = True


#Game Loop
while start:
    
    for _ in range(5):
    
        speak("Player one its your turn")
        pos = mycommand()
        if 'go' in pos:
            die_outcome = random.choice(die)
            print(f'The result of the die roll is {die_outcome}')
            print(f'The number of steps will be {20*die_outcome}')          
            player_one.fd(20*die_outcome)
            speak(f'player one has move {str(die_outcome)} steps')
            if player_one.pos() >= (300, 100):
                print("Player One has won the race!")
                speak('Player one has won the race')
                start = False
                break           
            elif player_two.pos() >= (300, -100):
                print("Player Two has won the race!")
                speak('Player two has won the race')
                start = False
                break
            break
        else:
            speak('Your command could not get understood')
            speak('Please repeat')
            continue
    
    for _ in range(5):
        speak("Player two its your turn")
        pos = mycommand()
        if 'go' in pos:
            die_outcome = random.choice(die)
            print(f'The result of the die roll is {die_outcome}')
            print(f'The number of steps will be {20*die_outcome}')
            player_two.fd(20*die_outcome)
            speak(f'player two has move {str(die_outcome)} steps')
            if player_one.pos() >= (300, 100):
                print("Player One has won the race!")
                speak('Player one has won the race')
                start = False
                break          
            elif player_two.pos() >= (300, -100):
                print("Player Two has won the race!")
                speak('Player two has won the race')
                start = False
                break
            break
        else:
            speak('Your command could not get understood')
            speak('Please repeat')
            continue


speak('You can close the window')    
window.mainloop()
