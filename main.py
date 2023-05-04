import os
from pynput.keyboard import Key, Listener
from pygame import mixer
import string

mixer.init()

sounds = os.listdir('sounds')

keys = {}

i = 0
for key in list(string.ascii_lowercase + string.digits + string.punctuation + r";'") + [str(i) for i in list(Key)]:
    keys[key] = sounds[i]
    i += 1

print(len(keys), 'keys')


def on_press(key):
    try:
        s = mixer.Sound('sounds/' + keys[str(key).replace("'", "")])
        s.play()
    except:
        print(key, 'not found')
        pass

    print(key, 'pressed')


with Listener(on_press=on_press) as listener:
    listener.join()
