class Pitcher(object):
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins
        self.base = 10000
    def __str__(self):
        return "%s (%s) / Wins : %d, Salary : $%d" % (self.name, "Pitcher", self.wins, self.getSalary())
    def getSalary(self):
        return self.wins * self.base

class Hitter(object):
    def __init__(self, name, batAvg = 0.0, hr = 0):
        self.name = name
        self.batAvg = batAvg
        self.hr = hr
        self.base1, self.base2 = 100000, 4000
    def __str__(self):
        return "%s (%s) / BatAvg : %.3f, HomeRuns : %d, Salary : $%d" % (self.name, "Hitter", self.batAvg, self.hr, self.getSalary())
    def getSalary(self):
        return self.batAvg * 100000 + self.hr * 4000

class Players(object):
    def __init__(self, p =[]):
        self.p = p
    def __str__(self):
        result=""
        for i in self.p:
            result = result + str(i) + "\n"
        return result

    def addPlayer(self, p):
        self.p.append(p)
    def sortPlayersBySalary(self):
        for i in range(len(self.p)):
            for j in range(i):
                if self.p[j].getSalary() < self.p[i].getSalary():
                    tmp = self.p[j]
                    self.p[j] = self.p[i]
                    self.p[i] = tmp

def loadPlayers(dataFile):
    player_list=[]
    f = open(dataFile, "r")
    for line in f:
        a = line.split(',')
        if a[1] == "Pitcher":
            player = Pitcher(a[0], int(a[2]))
        if a[1] == "Hitter":
            player = Hitter(a[0],float(a[2]), float(a[3]))
        player_list.append(player)
    return Players(player_list)

print ("--- Player Lists --- ")
players = loadPlayers("data.txt")
players.addPlayer(Pitcher("Oh", 5))
print(players)
players.addPlayer(Hitter("Park"))
print ("\n--- Player Lists (Sorted by Salary) --- ")
players.sortPlayersBySalary()
print(players)