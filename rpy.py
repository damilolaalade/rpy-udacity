import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        human_move = input('rock, paper, scissors ?')
        while human_move not in moves:
            human_move = input('enter again: rock, paper, scissors')
        return human_move


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class ImitatePlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def single_round(self):
        self.one_round = 1
        print("Sure, we will play 1 round")

    def multiple_rounds(self):
        self.multi_rounds = input('How many rounds do you want to play ?')
        while True:
            try:
                while int(self.multi_rounds) <= 1:
                    self.multi_rounds = input('Please enter a number'
                                              'greater than 1 :')
                if int(self.multi_rounds) > 1:
                    break
            except ValueError:
                self.multi_rounds = input('Please enter a number only:')
            print(f'Sure, we will play {self.multirounds} rounds.')

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            print('You have won this round')
            self.score1 += 1
            print(f'Player 1:{self.score1}, Player 2:{self.score2}\n')
        elif beats(move2, move1) is True:
            print('You have lost this round')
            self.score2 += 1
            print(f'Player 1:{self.score1}, Player 2:{self.score2}\n')
        else:
            print('This round is a tie')
            print(f'Player 1:{self.score1}, Player 2:{self.score2}\n')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        self.single = input('Do you want to play a single round?'
                            '[y/n]').lower()
        while self.single not in ["y", "n"]:
            self.single = input('Please enter either "y" or "n": ')
        if self.single == 'y':
            self.single_round()
            self.total_rounds = self.one_round
        elif self.single == 'n':
            self.multiple_rounds()
            self.total_rounds = self.multi_rounds
        print('\nGame Start!')
        for round in range(int(self.total_rounds)):
            print(f'Round {round + 1}:')
            self.play_round()
            print(f'Game over! Final Score :\
                  Player 1: {self.score1}, Player 2: {self.score2}')
            if self.score1 > self.score2:
                print('Yay, YOU WON')
            elif self.score1 < self.score2:
                print('Oops, YOU LOSE')
            else:
                print("IT'S A TIE")


if __name__ == '__main__':
    method = input('which of these methods would you like to use?\n\
        1. rock, 2. random, 3. imitate, 4. cycle.\n\
           Enter a number 1 to 4: ')
    while method not in ['1', '2', '3', '4']:
        method = input('Please Enter a number between 1 to 4')
    if method == '1':
        print('The player will always play rock.\n')
        game = Game(HumanPlayer(), Player())
        game.play_game()
    elif method == '2':
        print('The player will choose its moves randomly.\n')
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif method == '3':
        print('The player will imitate its'
              'moves just as in previous rounds.\n')
        game = Game(HumanPlayer(), ImitatePlayer())
        game.play_game()
    elif method == '4':
        print('The player will cycle through the'
              'moves in the previous rounds.\n')
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
