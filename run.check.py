
# run and check input/file


import os
import time

file_list = [
        '/tmp/rc.input',
        '~/tmp/rc.input'
        ]

import watchFile
import goo


def run_check(filename=None):
    if filename:
        return print('you give me a file name')

    lines = None
    monkey = watchFile.Monkey(file_list)

    condition = True
    while(True):
        #goo.searchGoogle() # as start point
        goo.pageCheck() 

        try:
            condition = input("x for exit: ")
            if condition == "x":
                break
        except:
            condition = 33

        if monkey.changed():
            lines = monkey.readFile()

        #time.sleep(1)

        if condition:
            print('got condition', condition)
            break
        if monkey.findStop():
            print('monkey find stop')
            break


if __name__ == "__main__":
    print("run and check")
    #run_check('name')
    run_check()

