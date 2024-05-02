##15.1 Exercise: Creating a class and an object

class Player:
    teamcolor = ''
    points = ''

team = Player()
team.teamcolor = 'Blue'
team.points = '300'
print('The',team.teamcolor, 'contenders has', team.points, 'points!' )
