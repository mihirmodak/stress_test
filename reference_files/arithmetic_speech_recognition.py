import sys
import subprocess
# implement pip as a subprocess
if sys.platform == "linux":
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

if sys.platform == "win32":
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyAudio-0.2.11-cp39-cp39-win_amd64.whl'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'speechrecognition~=3.8.1'])

import speech_recognition as sr
import random
import array

def one_digit_math():
    operation = random.randrange(1, 5) # random number from 1 to 4
    if (operation == 1): # addition
        number1 = random.randrange(10) # random number from 0 to 9
        number2 = random.randrange(10) # random number from 0 to 9
        print(f"What is {number1} + {number2}?") # print question
        answer = number1 + number2
    elif (operation == 2): # subtraction
        number1 = random.randrange(10) # random number from 0 to 9
        number2 = random.randrange(number1 + 1) # random number from 0 to number1+1
        print(f"What is {number1} - {number2}?") # print question
        answer = number1 - number2
    elif (operation == 3): # multiplication
        number1 = random.randrange(10) # random number from 0 to 9
        number2 = random.randrange(10) # random number from 0 to 9
        print(f"What is {number1} * {number2}?") # print question
        answer = number1 * number2
    elif (operation == 4): # division
        number1 = random.randrange(1, 10) # random number from 1 to 9
        # get the factors of number1
        factors = array.array('I',[]) # empty array of unsigned integers
        for i in range(1, number1 + 1):
            # for each number from 1 to number1
            if number1 % i == 0:
                factors.append(i) # add i to the list of factors
        factor_index = random.randrange(0, len(factors)) # get a random index
        number2 = factors[factor_index]
        print(f"What is {number1} / {number2}?") # print question
        answer = int(number1 / number2)
    else:
        # program should never get here
        answer = -1
    return answer

if __name__ == '__main__':
    try:
        r = sr.Recognizer() # recognizer instance
        r.pause_threshold = 0.5 # minimum length of silence after speaking
        r.energy_threshold = 200 # set energy threshold
        r.dynamic_energy_threshold = False # do not update ambient noise threshold

        with sr.Microphone() as m: # microphone instance
            print(f"Minimum energy threshold set to {r.energy_threshold}")
            while True: # forever and ever
                answer = one_digit_math() # get a random arithmetic problem
                questionAnswered = False
                while (questionAnswered == False):
                    with m as source: audio = r.listen(source)
                    try:
                        # recognize speech using Google Speech Recognition
                        value = r.recognize_google(audio)
                        try:
                            user_input = int(value)
                        except ValueError:
                            print("I can only understand numbers. Please repeat your answer.")
                        else:
                            questionAnswered = True
                            if (user_input == answer):
                                print(f"That's correct! The answer is {answer}")
                            else:
                                print(f"You said {user_input}, but the answer is {answer}")
                    except sr.UnknownValueError:
                        print("Oops! Didn't catch that")
                    except sr.RequestError as e:
                        print(f"Uh oh! Couldn't request results from Google Speech Recognition service; {e}")
    except KeyboardInterrupt:
        pass
