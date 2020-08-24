class SnakesLadders():
    import random

    def __init__(self, player = 1, position1 = 0, position2 = 0, turn = 0):
        self.turn = turn
        self.player = player
        self.position1 = position1
        self.position2 = position2

    def play(self, die1, die2):
        snakes = [16,46,49,62,64,74,89,92,95,99]
        ladders = [2,7,8,15,21,28,36,51,71,78,87]

        if self.position1 == 100 or self.position2 == 100:
            return "Game over!"

        if self.turn % 2 == 0:
            self.player = 1
            position = self.position1
        else:
            self.player = 2
            position = self.position2

        turn = self.turn
        player = self.player
        position = position + die1 + die2

        if position > 100:
            position = 100-(position-100)

        if position in snakes:
            position = self.snake(snakes.index(position))
        if position in ladders:
            position = self.ladder(ladders.index(position))

        if die1 != die2:
            self.turn = turn + 1

        if player == 1:
            self.position1 = position
        if player == 2:
            self.position2 = position

        if position == 100:
            return "Player %d Wins!" % (self.player)

        return "Player %d is on square %d" % (self.player,position)

    def snake(self,n):
        slideto = [6,25,11,19,60,53,68,88,75,80]
        return slideto[n]

    def ladder(self,n):
        climbto = [38,14,31,26,42,84,44,67,91,98,94]
        return climbto[n]
