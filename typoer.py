import keyboard
import random
from time import sleep

def typoer(text, wpm = 100, accuracy = 1, wait_key = '', break_key = ''):

    chars = list('abcdefghijklmnopqrstuvwxyz')

    if accuracy < 0:
        accuracy = 0
    elif accuracy > 1:
        accuracy = 1

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
        if typos and (i + typos >= len(text) or random.random() < 1 - 0.5 ** typos):
            sleep(0.2)
            for _ in range(typos):
                keyboard.press_and_release('backspace')
                sleep(0.2)
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


text = r'''Lorem Ipsum is simply dummy text of the printing and typesetting industry.'''


if __name__ == '__main__':
    typoer(text, wpm = 100, accuracy = 0.95, wait_key = 'up', break_key = 'down')
        
    