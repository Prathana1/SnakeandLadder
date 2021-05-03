import random


class Snake:

    def __init__(self):

        print('#' * 5 + 'Welcome to Snake & Ladders Game' + '#' * 5)
        self.name = input("Enter the Name of Player 1 : ")
        self.conf = input("Enter the Name of Player 2 : ")
        print('#' * 5 + 'Let us Start' + '#' * 5)
        self.game = [0, 0]

        self.Position_of_snakes = {17: 7, 54: 34, 62: 19, 98: 79}
        self.Position_of_ladders = {3: 38, 24: 33,  42: 93, 72: 84}

    def displayName(self):
        print(f"Name: {self.name} {self.conf}")

    def __winner__(self, number):
        if number == "1":
            winner = self.name
        else:
            winner = self.conf
        print("Player {} won the Game".format(number))
        print("Congratulations {} !!".format(winner))
        print('#' * 5 + 'Game successfully finished' + '#' * 5)
        exit(0)

    def __checkSnakeLadder__(self, position):

        if position in self.Position_of_snakes.keys():
            position = self.Position_of_snakes.get(position)
        elif position in self.Position_of_ladders.keys():
            position = self.Position_of_ladders.get(position)
        return position

    def __quitGame__(self, number):
        if number == "1":
            self.__winner__("2")
        else:
            self.__winner__("1")
        exit(0)

    def __checkMoreThanHundred(self, position, x):

        if(position + x) > 100:
            pass

        else:
            position += x
        return position

    def __checkManualMode__(self, inp):
        x = int(inp)
        if x not in range(2, 20):
            print(
                "invalid input! the number you enteres isn't within the range of between 1 and 20")
            x = int(input("please enter a number within the given range: "))
            return x

    def __checkMoveInput__(self, number):
        inp = input("Player {} : ".format(number))
        if inp == "roll":
            x = random.randint(1, 6)
        elif inp == "quit":
            self.__quitGame__(number)
        elif inp.isnumeric():
            x = self.__checkManualMode__(inp)
        else:
            print("illegal input, please input aa valid input!")
            x = self.__checkMoveInput__(number)
        print("you got a", x)
        return x

    def __playerPosition(self, number):

        pos = 0
        pos = self.game[int(number)-1]
        x = self.__checkMoveInput__(number)

        pos = self.__checkMoreThanHundred(pos, x)
        pos = self.__checkSnakeLadder__(pos)
        print(" Your Final Position is ", pos)
        if pos == 100:
            self.__winner__(number)
        self.game[int(number)-1] = pos

    def snakeGame(self):
        while True:
            self.__playerPosition('1')
            self.__playerPosition('2')


if __name__ == "__main__":

    snake = Snake()
    snake.snakeGame()
    del snake
