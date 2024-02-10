import sys
import random

def main():
    game()

def game():
    print('Lets start GuessTheNumvberGame!!!')
    min, max = inputNums()
    guessTheNumber(min, max)


def inputNums():
    min = 0
    max = 0
    
    while (True):
        sys.stdout.buffer.write(b'Input your minimum number ----> ')
        sys.stdout.flush()
        min = int(sys.stdin.buffer.readline().decode())

        sys.stdout.buffer.write(b'Input your max number ----> ')
        sys.stdout.flush()
        max = int(sys.stdin.buffer.readline().decode())

        if min <= max:
            print('Your input is correct!!')
            return min, max
        else:
            print('Your input is wrong!!')
            print('Minimum number should be less than max number')
            print('Input again!!')

def guessTheNumber(min, max):
    target = random.randint(min, max)
    answerLimit = random.randint(1, 10)

    print(f'target is created. You can answer {answerLimit} times.')

    cnt = 1
    while cnt <= answerLimit:
        sys.stdout.buffer.write(b'Input your predict num ---> ')
        sys.stdout.flush()
        preNum = int(sys.stdin.buffer.readline())

        if preNum == target:
            print('Your answer is correct. You win!!!!')
            sys.exit()
        else:
            if answerLimit - cnt == 0: break

            print(f'Your answer is wrong. You can answer {answerLimit - cnt} times.')
        
        cnt += 1

    print(f'You loose!!! The target is {target}')
    sys.exit()

if __name__ == '__main__':
    main()