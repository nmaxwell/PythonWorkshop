
class Planet(object):
    def __init__(self, name, position, population):
        self.name = name
        self.position = position
        self.population = population

    def explode(self):
        print "planet '%s' breaks apart into chunks, spilling %s dead bodies into space" % (self.name, self.population)

class Star(object):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def explode(self):
        print "star '%s' destroyed" % self.name


class DeathStar(object):
    def __init__(self, position):
        self.position = position

    def fire_death_ray(self, target):
        print distance(self.position, target.position)
        if distance(self.position, target.position) < 10:
            print "deathstar fires laser at %s" % target.name
            target.explode()
        else:
            print "deathsar is out of range to hit %s " % target.name

def distance(x1,x2):
    import math
    return math.sqrt((x1[0] - x2[1]) ** 2 + (x1[0] - x2[1]) ** 2)

alderaan = Planet('alderaan',[0,0], 50)
death_star = DeathStar([1,1])

death_star.fire_death_ray(alderaan)
