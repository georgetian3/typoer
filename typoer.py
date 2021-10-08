import keyboard
import random
from time import sleep

# text: the text to be typed
# wpm: average typing speed, measured in words per minute
# accuracy: float between 0 and 1, higher accuracy means less typos
# backspace_duration: time taken for backspace to be pressed
# correction_coefficient: determines how many typos are made before correcting them,
#                         lower coefficient means typos are caught quicker
# wait_key: press this key to start typing
# break_key: press this key to stop typing


def typoer(text, wpm = 100, accuracy = 1, backspace_duration = 0.1, correction_coefficient = 0.4, wait_key = '', break_key = 'escape'):

    chars = list('abcdefghijklmnopqrstuvwxyz')

    # seconds per character, using the average of 5 characters per word
    spc = 12 / wpm
    # determines how much the spc varies between characters
    spc_range = 0.8
    # as humans don't type at a constant rate, allow sleep duration between chars to vary
    spc_low = spc * (1 - spc_range)
    spc_high = spc * (1 + spc_range)

    i = 0
    typos = 0

    if wait_key:
        keyboard.wait(wait_key)

    while i < len(text):

        if keyboard.is_pressed(break_key):
            return

        # correct typos
        if typos and (i + typos >= len(text) or random.random() < 1 - correction_coefficient ** typos):
            sleep(backspace_duration)
            for _ in range(typos):
                keyboard.press_and_release('backspace')
                sleep(backspace_duration)
            typos = 0
        # make typo
        if random.random() > accuracy: 
            keyboard.write(random.choice(chars))
            typos += 1
        # type correct char
        else: 
            keyboard.write(text[i + typos])
            if typos:
                typos += 1
            else:
                i += 1

        duration = random.uniform(spc_low, spc_high)

        sleep(duration)



if __name__ == '__main__':
    text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    typoer(text, wpm = 120, accuracy = 0.8, wait_key = 'right')
        
    
