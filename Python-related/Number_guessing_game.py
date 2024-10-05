import random

class NumberGuessGame():
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.secret_Num = random.randint(start,end)
        self.count = 0

    def make_guess(self,guess):
        if self.count < 5:
            self.count = self.count + 1
            print(f'Count: {self.count}')
            if guess > self.secret_Num:
                print("It's too Large Number that you have guessed")
                return True
            elif guess < self.secret_Num:
                print("It's too small Number that you have guessed")
                return False
            elif guess == self.secret_Num:
                print("You had done guessing the number")
                print(f'You had done in {self.count} chances')
                return "won"
        else:
            print(f'You have completed {self.count} choices')
            return "lost"


    def play(self):
        print(f'Enter Number range from {self.start} and {self.end}')
        while True:
            try:
                guess = int(input("Enter a Number that you need to Guess: "))
                res = self.make_guess(guess)
                if(res=="won"):
                    print("----------Congratulations you won!------------------")
                    return
                elif(res=="lost"):
                    print("-----Sorry You Lost this game try again----")
                    return
                print(res)
            except ValueError:
                print("Please enter a valid integer!..")

start = 1
end = 100
game = NumberGuessGame(start,end)
game.play()