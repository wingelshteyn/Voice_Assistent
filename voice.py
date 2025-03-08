import random

import winsound
from app import tts

r = random.Random()

def speaker(text):
    fragments = text.split('|')
    fragment = fragments[r.randint(0, len(fragments)-1)]

    tts.tts(fragment, "output.wav")

    filename = 'output.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)
