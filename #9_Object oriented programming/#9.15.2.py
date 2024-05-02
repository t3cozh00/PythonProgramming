#15.2 Exercise: Creating a method

class Player:
    __teamcolor = 'Blue'
    __points = 0

    def tellscore(self):
        print('I am', self.__teamcolor, ', we have', self.__points, 'points!')
    def goal(self, value = 1):
        self.__points =+ value



team = Player()
team.goal()
team.tellscore()
