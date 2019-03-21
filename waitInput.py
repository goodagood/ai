
# todo: prepare variables to run into interpretor
# adjust text with NLTK sentence tokenizer

import select
import sys

print('Press enter to continue.', end='', flush=True)
r, w, x = select.select([sys.stdin], [], [], 600)

def waitUser(msg="\ninput here: ", timeout=2):
    print(msg, end='', flush=True)
    r, w, x = select.select([sys.stdin], [], [], timeout)
    if r:
        i = sys.stdin.readline().strip()
        return i
    else:
        return None


def xMeansExit():
    i = waitUser(msg="\n input here, x means EXIT, 15 seconds...: ", timeout=15)
    #print('we got input: ', i)
    if i == 'x':
        sys.exit()
    else:
        return i


