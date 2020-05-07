import random
import time


def evaluate(answer, guess):
    # evaluate guess by the rule of baseball game.
    # answer type : Inteager
    # guess type : Inteager
    # return value : Tuple of (int, int)
    # ex : evaluate(123, 324) -> (1, 1)
    guess = str(guess)
    answer = str(answer)
    ball = 0
    strike = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1
    return strike, ball


def generate_answer(k):
    # generate length k inteager for baseball game.
    # No repeatation in the number.
    # k : Inteager 1~9
    # return value : k length inteager
    # ex : generate_answer(4) -> 5936
    n = list(range(1, 10))
    random.shuffle(n)
    result = 0
    for i in range(k):
        result += n[i] * (10 ** i)
    return result


def get_guess(k):
    # get user input for guess
    # k : Inteager 1~9
    # return value : k length inteager
    while True:
        guess = input("WHAT IS YOUR GUESS? : ")
        if len(guess) != k or not guess.isdigit():
            print("Your guess should be %d length inteager!!" % k)
        elif '0' in guess:
            print("Your guess should not contain 0!!")
        elif len(list(guess)) != len(set(guess)):
            print("Your guess should not contain repeated number!!")
        else:
            return int(guess)


def play_baseball(k):
    print("BASEBALL GAME START!!")
    print("I'm generating %d-length answer." % k)
    answer = generate_answer(k)
    time.sleep(2)
    trial = 0
    print("LET'S START THE GAME!!")
    while True:
        trial += 1
        guess = get_guess(k)
        strike, ball = evaluate(answer, guess)
        if strike == k:
            print("HOOOME RUUUN!!!!!!")
            print("You got the answer in %d times" % trial)
            return trial
        if strike == 0 and ball == 0:
            print("OUT!!")
        else:
            if strike == 0:
                strike = ""
            else:
                strike = str(strike) + "STRIKE"
            if ball == 0:
                ball = ""
            else:
                ball = str(ball) + "BALL"
            print("GUESS : %d ==>" % guess, strike, ball)


game_result = []
while True:
    length = random.randrange(3, 4)
    trial = play_baseball(length)
    game_result.append((length, trial))
    M = input("DO YOU WANT TO PLAY MORE? Y/N ")
    if M == "N":
        for i in enumerate(game_result):
            g = ""
            if i[0] == 0:
                g = "  1st game"
            elif i[0] == 1:
                g = "  2nd game"
            elif i[0] == 2:
                g = "  3rd game"
            else:
                g = "  %d-th game" % (i[0]+1)
            print(g, ": %d length, got the answer in %3d trial." % (i[1][0], i[1][1]))
        break
