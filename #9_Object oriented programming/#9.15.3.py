##15.3 Exercise: Initializing a class
class Player:
    """Player-class: stores data on team colors and points."""

    __teamcolor = ''
    __points = 0

    def __init__(self):
        self.__teamcolor = input('What color do I get?: ')

    def tellscore(self):
        print('I am', self.__teamcolor, ', we have', self.__points, 'points!')
    def goal(self, value = 1):
        self.__points += value

player1 = Player()
player2 = Player()
player1.goal()
player1.goal()
player2.goal()
player1.tellscore()
player2.tellscore()