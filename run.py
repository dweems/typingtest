import random
import threading
import os

def you_lost():
    print("Sorry, you were too slow!")
    os._exit(1)

def init_game(words):
    try:
        score = 0
        while True:
            if score == 9010:
                print("IT'S OVER 9000!!!!!!!!!!!!!!!")

            word = random.choice(words)
            t=threading.Timer((10.0-(score/100)),you_lost)

            t.start()
            typed_word = input("{}: ".format(word))
            t.cancel()

            if typed_word == word:
                score=score+10
                print("match! Score: {}".format(score))
            else:
               score=score-10
               print("not a match! Score: {}".format(score))


    except KeyboardInterrupt:
        t.cancel()
        print('\nYou are a quiter.')


if __name__ == '__main__':
    with open('/usr/share/dict/words', 'r') as file:
        words=file.read().replace('\n', ' ').split()
    init_game(words)
