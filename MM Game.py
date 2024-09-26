import random

num = str(random.randint(1000,10000))
print(num)
print('You have total of 3 tries to guess the number')
n = str(int(input("Guess a four digit number: ")))


while len(n) !=  4  :
    n = str(int(input("Guess only a four digit number: ")))
else :
    turn = 3
    if num == n :
            print("You guessed the correct number in first try! You are real Mastermind!")

    else:

        while num != n :
            if len(n) == 4 :
                turn -=1
                turnx = 4 - turn
                if turn < 1:
                    print(f'You lost! The number is "{num}". ')
                    break
                else :
                    for i in range (0,4):
                        if num[i] == n[i]:
                                print(n[i])

                        else :
                            print('X')
                print(f'You have {turn} try left!')
                n = str(int(input("Guess a four digit number: ")))

                if num == n :
                     print(f"You guessed the correct number in {turnx} tries ! You are the Mastermind!")
                     break

            else :
                n = str(int(input("Guess a four digit number: ")))




























































































