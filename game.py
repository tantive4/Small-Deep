import model

class Board():
    def __init__(self) :
        return
    
board = Board()

class ship :
    def __init__(self, type, self_x, self_y, direction, speed) :
        self.type = type
        self.hull = type.get('hull')
        self.point = type.get('point')
        self.CommandValue = type.get('command')
        self.SquadronValue = type.get('squadron')
        self.EngineeringValue = type.get('engineering')
        self.AntiSquad = type.get('anti_squad')
        self.FrontDice = type.get('battery')[0]
        self.LeftDice = type.get('battery')[1]
        self.RightDice = type.get('battery')[1]
        self.RearDice = type.get('battery')[2]

        self.speed = speed
        self.navchart = type.get('speed')
        self.activated = False
        self.damage = 0
        self.critical = [0 for i in range(22)]

        self.x = self_x
        self.y = self_y
        self.direction = direction
        self.CommandStack = []
        self.CommandToken = [0, 0, 0, 0] # [nav, squadron, engineering, concentrate fire]

        
        self.front = type.get('shield')[0]
        self.left = type.get('shield')[1]
        self.right = type.get('shield')[1]
        self.rear = type.get('shield')[2]
        self.defense = {i : [type.get('defense')[i], 1] for i in range(len(type.get('defense')))}

    def set_command(self, command) : # [nav, squadron, engineering, concentrate fire] ex) [1,0,0,0]
        self.CommandStack.append(command)


    def activate(self) :
        self.activated = True

        # reveal command dial
        self.CommandDial = self.CommandStack.pop(0) if self.CommandStack else [0, 0, 0, 0]
        if model.DialtoToken(board, self.CommandDial, self.CommandToken) :
            self.CommandToken += self.CommandDial
            self.CommandToken = [min(1, i) for i in self.CommandToken]
            self.CommandDial = [0, 0, 0, 0] # reset command to 0

        if (self.CommandDial + self.CommandToken)[1] > 0 :
            squadActivate = model.SquadCommand(board, self.CommandDial[1], self.CommandToken[1], self.SquadronValue)
            if squadActivate > self.SquadronValue :
                self.CommandToken[1] = 0 # reset squadron token if exceed squadron value
            
            while squadActivate > 0 :
                model.SquadronCommand()
                squadActivate -= 1
            
        if (self.CommandDial + self.CommandToken)[2] > 0 :
            engineerPoint = model.EngineerCommand(board, self.CommandDial[2], self.CommandToken[2], self.EngineeringValue)
            if engineerPoint > self.EngineeringValue :
                self.CommandToken[2] = 0 # reset engineering token if exceed engineering value




        # attack

        # manuver


# attack dice = [black, blue, red]
victory_1 = {
    'size' : 'medium',
    'hull' : 8,
    'command' : 3,
    'squadron' : 3,
    'engineering' : 4,
    'defense' : ['brace', 'redirect', 'redirect'],
    'anti_squad' : [0, 1, 0],
    'shield' : [3, 3, 1],
    'battery' : [[3, 0, 3], [1, 0, 2], [0, 0, 2]],
    'speed' : {1 : [1], 2 : [0, 1]},
    'point' : 73
    }

victory_2 = {
    'hull' : 8,
    'command' : 3,
    'squadron' : 3,
    'engineering' : 4,
    'defense' : ['brace', 'redirect', 'redirect'],
    'anti_squad' : [0, 1, 0],
    'shield' : [3, 3, 1],
    'battery' : [[0, 3, 3], [0, 1, 2], [0, 0, 2]],
    'speed' : {1 : [1], 2 : [0, 1]},
    'point' : 80
    }

CR90A = {
    'hull' : 4,
    'command' : 1,
    'squadron' : 1,
    'engineering' : 2,
    'defense' : ['evade', 'evade', 'redirect'],
    'anti_squad' : [0, 1, 0],
    'shield' : [2, 2, 1],
    'battery' : [[0, 1, 2], [0, 1, 1], [0, 0, 1]],
    'speed' : {1 : [2], 2 : [1, 2], 3 : [0, 1, 2], 4 : [0, 1, 1, 2]},
    'point' : 44
    }

CR90B = {
    'hull' : 4,
    'command' : 1,
    'squadron' : 1,
    'engineering' : 2,
    'defense' : ['evade', 'evade', 'redirect'],
    'anti_squad' : [0, 1, 0],
    'shield' : [2, 2, 1],
    'battery' : [[0, 3, 0], [0, 2, 0], [0, 1, 0]],
    'speed' : {1 : [2], 2 : [1, 2], 3 : [0, 1, 2], 4 : [0, 1, 1, 2]},
    'point' : 39
    }

Neb_escort = {
    'hull' : 5,
    'command' : 2,
    'squadron' : 2,
    'engineering' : 3,
    'defense' : ['evade', 'brace', 'brace'],
    'anti_squad' : [0, 2, 0],
    'shield' : [3, 1, 2],
    'battery' : [[0, 0, 3], [0, 1, 1], [0, 0, 2]],
    'speed' : {1 : [1], 2 : [1, 1], 3 : [0, 1, 2]},
    'point' : 47
    }

Neb_support = {
    'hull' : 5,
    'command' : 2,
    'squadron' : 1,
    'engineering' : 3,
    'defense' : ['evade', 'brace', 'brace'],
    'anti_squad' : [0, 1, 0],
    'shield' : [3, 1, 2],
    'battery' : [[0, 0, 3], [0, 1, 1], [0, 0, 2]],
    'speed' : {1 : [1], 2 : [1, 1], 3 : [0, 1, 2]},
    'point' : 51
    }

ship1 = ship(victory_1, 0, 0, 0, 1)
ship2 = ship(victory_2, 0, 0, 0, 1)
ship3 = ship(CR90A, 0, 0, 0, 1)
ship4 = ship(CR90B, 0, 0, 0, 1)
ship5 = ship(Neb_escort, 0, 0, 0, 1)
ship6 = ship(Neb_support, 0, 0, 0, 1)


