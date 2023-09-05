from random import *
#made by Braybuss
def mapping():
    pass
    #project for later to use unicode to make dungeon
def line(n):
    i = n
    while i > 0:
        print("\n")
        i -= 1

def cheqDeath():
    for char in chars:
        if char.hp <= 0:
            if char in enemies:
                enemies.remove(char)
            print("{0} has died".format(char.name))
            chars.remove(char)

def newchar(y,poopsocks):
    bozo = True
    #dmg, dmgvar, range, speed, hp, spellz, recoverz, name, pos
    while bozo == True:
        match input("What class will your {0} character be?(input number)\n>>>".format(poopsocks)):
            case "1":
                bozzo = True
                while bozzo == True:
                    match input("Would you like a sword fighter(1), crossbow fighter(2) or a bowman(3)? the more rangs(bowman has most) the less damage and hp. bowman and crossbow fighter have medium movement\n>>>"):
                        case "1":#sword
                            bozzo = False
                            bozo = False
                            return Playerchar(11,2,1,3,18,0,6,input("What will you name your sword fighter?(suggested 5 characters)\n>>>"),[0,y])

                        case "2":#crosbow
                            bozzo = False
                            bozo = False
                            return Playerchar(10,2,2,2,15,0,5,input("What will you name your crossbow fighter?(suggested 5 characters)\n>>>"),[0,y])

                        case "3":#archer
                            bozzo = False
                            bozo = False
                            return Playerchar(9,1,3,2,12,0,4,input("What will you name your bowman?(suggested 5 characters)\n>>>"),[0,y])

                        
            case "2":#barb
                bozo = False
                return Playerchar(8,2,1,2,25,0,8,input("What will you name your barbarian?(suggested 5 characters)\n>>>"),[0,y])
            case "3":#wiz
                bozo = False
                return Playerchar(10,1,5,1,12,3,4,input("What will you name your wizard?(suggested 5 characters)\n>>>"),[0,y]) 
            case "4":#cleric
                bozo = False
                return Playerchar(6,1,3,1,16,2,6,input("What will you name your cleric?(suggested 5 characters)\n>>>"),[0,y])
            case "5":#sorc
                bozo = False
                return Playerchar(8,1,4,1,15,1,4,input("What will you name your sorcerer?(suggested 5 characters)\n>>>"),[0,y])
            case _:
                print("Invalid, try again")


def battmap():
    #Unicode characters for walls later, will look much better ║, ╠, ═, ╣, ╬, ╦ , ╩
    #CORNERS ╚, ╗, ╝, ╔
    #DOORS? ┋, ┈┈┈
    #DONT KNOW NORMAL TILES(|░░░|?)  ▓ for blokced areas? 
    #                        ░░░ ░░░
    #the following might be usefull,   ▨，▧，▦，▩， ◎， ◍， 
    y0 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y1 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y2 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y3 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y4 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y5 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y6 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y7 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y8 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    y9 =  ['_____','_____','_____','_____','_____','_____','_____','_____','_____','_____']
    ylvz = [y0,y1,y2,y3,y4,y5,y6,y7,y8,y9]
    for char in chars:
        ylvz[char.pos[1]][char.pos[0]] = char.name
        #matches so fun, why do I need to be efficient XD
        #match char.pos[0]:
            #case 0:
             #   y0[char.pos[1]] = char.name
   #         case 1:
    #            y1[char.pos[1]] = char.name
     #       case 2:
     #           y2[char.pos[1]] = char.name
     #       case 3:
     #           y3[char.pos[1]] = char.name
     #       case 4:
     #           y4[char.pos[1]] = char.name
     #       case 5:
     #           y5[char.pos[1]] = char.name
     #       case 6:
     #           y6[char.pos[1]] = char.name
     #       case 7:
     #           y7[char.pos[1]] = char.name
     #       case 8:
     #           y8[char.pos[1]] = char.name
    #        case 9:
   #             y9[char.pos[1]] = char.name
    for ylev in ylvz:
        print('  '.join(ylev))
            
class Playerchar:
    def __init__(self, damage,dmgvar,attrnge,spd,hp,spellz,recoverz,name,pos):
        #damage base stat
        self.damage = damage
        #variability on damage
        self.dmgvar = dmgvar
        #attack range
        self.attrnge = attrnge
        #amount of tiles a character can move in a turn
        self.spd = spd
        #health a character has
        self.hp = hp
        self.Maxhp = hp
        #how accurate the character is
        self.spellz = spellz
        #how hard it is to hit character
        self.recoverz = recoverz
        #name of character on map
        self.name = name
        self.pos = pos

    def turn(self):
        donezoe = False
        turnct = 3
        anum = 0
        rnum = 0
        if self.spellz > 0:
            casted = False
            while turnct > 0:
                print("{0} actions left".format(turnct))
                donezoe = False
                while donezoe == False:
                    match input("What would {0} like to do? Move(m){1} has a speed of {2}, attack(a){3} has a range of {4}(no diagonals) or cast(c)(can return if you do not want to cast)\n>>>".format(self.name,self.name,self.spd,self.name,self.attrnge)):
                        case "m":
                            self.move()
                            donezoe = True
                            turnct -=1
                        case "a":
                            if self.attack(anum):
                                print("No targets!")
                            else:
                                turnct-=1
                                donezoe = True
                                anum += 1
                        case "c":
                            result = self.cast(turnct)
                            if result == True:
                                print("Returning, you may choose a new action")
                            else:
                                turnct -= int(result)
                                donezoe = True
                                casted = True
            if casted == False:
                self.recoverz += 1
                print("{0} Regained one mana, now at {1}".format(self.name, self.recoverz))
                        
                                
        else:
            while turnct > 0:
                print("{0} actions left".format(turnct))
                donezoe = False
                while donezoe == False:
                    match input("What would you like to do? Move(m){0} has a speed of {1}, attack(a){2} has a range of {3}(no diagonals) or recover(r)(will recover {4} hp)\n>>>".format(self.name,self.spd,self.name,self.attrnge,self.recoverz-rnum*2)):
                        case "m":
                            self.move()
                            donezoe = True
                            turnct -= 1
                        case "a":
                            if self.attack(anum):
                                print("No targets!")
                            else:
                                donezoe = True
                                anum += 1
                                turnct -= 1
                        case "r":
                            self.recover(rnum)
                            rnum +=1
                            turnct -=  1
                            donezoe = True

    def cast(self,turnct):
        print("{0} has {1} mana remaining".format(self.name,self.recoverz))
        match self.spellz:
            case 1: #sorcerer
                print("1:Fire bolt            Actions:1 Mana:1")
                print("2:ice knife            Actions:1 Mana:1")
                print("3:minor heal           Actions:1 Mana:2")
                #print("4:      Actions:1 Mana:3")
                #print("5:minor damage bootst  Actions:2 Mana:3")
                #print("6:fireball             Actions:2 Mana:4")
                bozo = True
                while bozo == True:
                    spell = input("Give int of spell you want to do, to b to go back. {0} has {1} mana remaining\n>>>".format(self.name, self.recoverz))
                    match spell:
                        case "1":
                            bozo = False
                            if self.recoverz > 0:
                                self.attrnge += 1
                                if self.attack(-3):
                                    self.attrnge -= 1
                                    return True
                                else:
                                    self.attrnge -= 1
                                    self.recoverz -= 1
                                    return "1"
                                
                        case "2":
                            bozo = False
                            if self.recoverz > 0:
                                if self.iceKnife() == True:
                                    print("No targets")
                                else:
                                    bozo = False
                                    self.recoverz -= 1
                                    return "1"
                        case "3":
                            bozo = False
                            if self.recoverz > 1:
                                self.minorHeal()
                                self.recoverz -= 2
                                return "1"
                        case "4":
                            bozo = False
                            print("Not an option right now, sorry")
                            return True
                        case "5":
                            bozo = False
                            print("Not an option right now, sorry")
                            return True
                        case "b":
                            print("Going back!")
                            return True
            case 2: #cleric
                print("1:radiant bolt         Actions:1 Mana:1")
                print("2:speed boost          Actions:1 Mana:1")#make temporary?
                print("3:bane                 Actions:1 Mana:2")
                print("4:minor heal           Actions:1 Mana:2")
                #print("5:minor damage boost   Actions:2 Mana:3")
                #print("6:mass heal            Actions:2 Mana:4")
                spell = input("Give int of spell you want to do, to b to go back. {0} has {1} mana remaining\n>>>".format(self.name, self.recoverz))
                match spell:
                    case "1":
                        if self.recoverz > 1:
                            self.attrnge += 2
                            if self.attack(-3):
                                self.attrang -= 2
                                return True
                            else:
                                self.recoverz -= 1
                                self.attrnge -= 2
                                return "1"
                        else:
                            print("You do not have enough mana. you can get more by not casting a spell on a characters turn")
                    case "2":
                        if self.recoverz > 0:
                            self.speedBoost()
                            self.recoverz -= 1
                            return "1"
                        else:
                            print("Not enough mana")                            
                            
                    case "3":
                        if self.recoverz > 1:
                            self.attrnge += 3
                            if self.Bane() is False:
                                print("No targets to bane")
                                return True
                            self.recoverz -= 2
                            self.attrnge -= 3
                            return "1"
                        else:
                            print("Not enough mana")
                    case "4":
                        if self.recoverz > 1:
                            self.minorHeal()
                            self.recoverz -= 2
                            return "1"
                        else:
                            print("Not enough mana")
                    case "5":
                        print("Not an option yet")
                        return True
                    case "6":
                        print("Not an option yet")
                        return True
                    case "b":
                        return True
            case 3: #Wizard
                print("1:Fire bolt            Actions:1 Mana:1")
                print("2:ice knife            Actions:1 Mana:1")
                #print("3:entangle             Actions:1 Mana:2")
                print("4:ray of fire          Actions:2 Mana:3")
                #print("5:fireball             Actions:2 Mana:4")
                #print("6:Lightning strike     Actions:3 Mana 6:")
                spell = input("Give int of spell you want to do, to b to go back. {0} has {1} mana remaining\n>>>".format(self.name, self.recoverz))
                match spell:
                    case "1":
                        if self.recoverz > 0:
                            self.attrnge += 1
                            if self.attack(-2):
                                pass
                            else:
                                self.attrnge -= 1
                                return "1"
                            self.attrnge -= 1
                    case "2":
                        if self.recoverz > 0:
                            self.attrnge += 1
                            if self.iceKnife() == True:
                                self.attrnge -= 1
                            else:
                                self.attrnge -= 1
                                return "1"
                        else:
                            print("you do not have enough mana")
                            return True
                    case "3":
                        print("Not an option right now, sorry")
                        return True
                    case "4":
                        if self.recoverz > 2:
                            if turnct > 1:
                                self.attrnge += 22
                                self.rayOFire()
                                self.attrnge -= 22
                                return "2"
                            else:
                                print("not enough actions")
                                return True
                        else:
                            print("you do not have enough mana to cast this spell")
                            return True
                    case "5":
                        print("Not an option right now, sorry")
                        return True
                    case "6":
                        print("Not an option right now, sorry")
                        return True
                    case "b":
                        return True

    def iceKnife(self):
        options = self.detect(enemies)
        if len(options) < 1:
            return True
        target = int(input("what will you hit with Ice knife?\n>>>"))
        target = options[target-1]
        print("{0} has been selected".format(target.name))
        target.hp -= 6
        print("6 damage to {0}, and has reduced their speed".format(target.name))
        target.spd -= 1
        cheqDeath()
        
        

    def minorHeal(self):
        options = self.detect(pchars)
        if len(options) < 1:
            return True
        print("3: {0}".format(self.name))
        options.append(self)
        target = int(input("Who would you like to heal?\n>>>"))
        target = options[target-1]
        target.hp += 6
        if target.hp > target.Maxhp:
            target.hp = target.Maxhp
        print("{0} has been healed to {1} hp!".format(target.name,target.hp))

    def speedBoost(self):
        self.attrnge += 22
        options = self.detect(pchars)
        bozo = True
        while bozo == True:
             try:
                 target = int(input("Who would you like to target for the speed boost?\n>>>"))
             except:
                 print("invalid input")
             else:
                 bozo = False
        target = options[target-1]
        target.spd += 1
        print("{0} has had a speed increase to {1}".format(target.name,target.spd))
        self.attrnge -= 22


    def Bane(self):
        bozo = True
        options = self.detect(enemies)
        if len(options) < 1:
            print("No targets!")
            return False
        while bozo == True:
            try:
                target = int(input("Who would you like to target for bane?\n>>>"))
            except:
                print("invalid input")
            else:
                bozo = False
        target = options[target-1]
        target.damage -= 2
        print("you reduced {0}'s damage to {1}".format(target.name,target.damage))

    def entangle(self):
        pass
    def rayOFire(self):
        options = self.detect(enemies)
        bozo = True
        while bozo == True:
            try:
                target = int(input("Who would you like to target?(you will then choose horizontal or vertical)\n>>>"))
            except:
                print("invalid input")
            else:
                bozo = False

        target = options[target-1]
        while bozo == False:
            match input("Horizontal(h) or verticle(v)\n>>>"):
                case "h":
                    for char in chars:
                        if char.pos[1] == target.pos[1]:
                            if char in pchars:
                                char.hp -=4
                                print("you did 4 damage to {0}(now at {1})".format(char.name,char.hp))
                            else:
                                char.hp -= 9
                                print("you did 9 damage to {0}".format(char.name))
                            cheqDeath()
                            bozo = True
                case "v":
                    for char in chars:
                        if char.pos[0] == target.pos[0]:
                            if char in pchars:
                                char.hp -=4
                                print("you did 4 damage to {0}(now at {1})".format(char.name,char.hp))
                            else:
                                char.hp -= 9
                                print("you did 9 damage to {0}".format(char.name))
                            cheqDeath()
                            bozo = True
                case _:
                    print("Not an option")
        pass
    def detect(self,chars):
        options = []
        for char in chars:
            if self.name == char.name:
                pass
            else:
                if abs(self.pos[0]-char.pos[0])+ abs(self.pos[1]-char.pos[1]) <= self.attrnge:
                    options.append(char)
                else:
                    print("{0} is not in range".format(char.name))
        count = 0
        for char in options:
            count += 1
            print("{0}: {1}".format(count,char.name))
        return options
                   
            

    
    def recover(self,num):
        print("Recovering!")
        self.hp += self.recoverz - num*2
        if self.hp > self.Maxhp:
            self.hp = self.Maxhp
            print("{0} healed to max(1)!".format(self.name,self.hp))
        else:
            print("{0} is now at {1} Hp!".format(self.name,self.hp))
                        
    def move(self):
        donezoe = True
        movespd = self.spd
        while movespd > 0:
            print("{0} movement remaining".format(movespd))
            match input("Up(u), Down(d), Left(l), Right(r) or pass(p)\n>>>"):
                case "u":
                    self.pos[1] -= 1
                    movespd -= 1
                    battmap()
                    print("Moving up!")
                    if self.pos[1] < 0:
                        print("You cannot move up right now")
                        self.pos[1] += 1
                        donezoe = False
                        movespd += 1
                        
                    for char in chars:
                        if char.pos[0] == self.pos[0] and char.pos[1] == self.pos[1]:
                            if char.name == self.name:
                                pass
                            else:
                                print("You may not move up, there is something in the way!")
                                self.pos[1] += 1
                                donezoe = False
                                movespd += 1

                            
                    donezoe = True
                case "d":
                    self.pos[1] += 1
                    movespd -= 1
                    print("Moving down!")
                    if self.pos[1] > 9:
                        print("You cannot move down right now")
                        self.pos[1] -= 1
                        donezoe = False
                        movespd += 1
                        
                    for char in chars:
                        if (char.pos[0] == self.pos[0] and char.pos[1] == self.pos[1]):
                            if char.name == self.name:
                                pass
                            else:
                                print("You may not move down, there is something in the way!")
                                self.pos[1] -= 1
                                movespd += 1
                                donezoe = False
                    battmap()
                    donezoe = True    
                case "l":
                    self.pos[0] -= 1
                    movespd -= 1
                    print("Moving left!")
                    
                    if self.pos[0] < 0:
                        print("You cannot move left right now")
                        self.pos[0] += 1
                        movespd += 1
                        donezoe = False
                    for char in chars:
                        if char.pos[0] == self.pos[0] and char.pos[1] == self.pos[1]:
                            if char.name == self.name:
                                pass
                            else:
                                print("You may not move left, there is something in the way!")
                                self.pos[0] += 1
                                donezoe = False
                                movespd += 1
                    donezoe = True
                    battmap()
                case "r":
                    self.pos[0] += 1
                    movespd -= 1
                    print("Moving right!")
                    if self.pos[0] > 9:
                        print("You cannot move right right now")
                        self.pos[0] -= 1
                        donezoe = False
                        movespd += 1
                    for char in chars:
                        if char.pos[0] == self.pos[0] and char.pos[1] == self.pos[1]:
                            if char.name == self.name:
                                pass
                            else:
                                print("You may not move right, there is something in the way!")
                                self.pos[0] -= 1
                                donezoe = False
                                movespd += 1
                    donezoe = True
                    battmap()
                    
                case "p":
                    movespd = 0
                    battmap()
                    print("Voiding rest of movement")
                    
                    

    def attack(self,anum):
        count = 0
        options = []
        for enemy in enemies:
            if enemy.pos == False:
                pass
            if abs(enemy.pos[0]-self.pos[0]) + abs(enemy.pos[1]-self.pos[1]) <= self.attrnge:
                options.append(enemy)
                count += 1
                print(str(count)+ ":" + enemy.name)
        if count == 0:
            print("No targets!")
            return True
        target = count + 2
        while int(target) > count:
            try:
                target = int(input("What would you like to attack?(Give number)\n>>>"))
            except:
                print("Not a valid input")
            if target > count:
                print("not a target!")
            elif target <= 0:
                print("not a target!")
                target = count + 2
        var = round(randint(0,self.dmgvar))
        direction = round(randint(-1,1))
        var = var*direction
        damage = self.damage + var - anum*2
        options[count-1].hp -= damage
        print("attacking {0}".format(options[count-1].name))
        print("you did {0} damage!".format(damage))
        battmap()

        for char in chars:
            if char.hp <= 0:
                if char in enemies:
                    enemies.remove(char)
                print("{0} has died".format(char.name))
                chars.remove(char)

                


        
class goblin:
    def __init__(self,damage,hp,ID,pos,attrnge):
        self.damage= damage
        self.hp = hp
        self.ID = ID
        self.pos = pos
        self.attrnge = attrnge
        self.name = "gobf "
        if self.attrnge > 1:
            self.name = "goba "
        self.name += str(ID)
        self.spd = 3
    def move(self):
        distance = []
        for char in pchars:
            distance.append(abs(self.pos[0]-char.pos[0])+abs(self.pos[1]-char.pos[1]))
        goto = min(distance)
        goto = distance.index(goto)
        print("moving to char: " + str(goto+1))
        movement = self.spd
        xdif = abs(pchars[goto].pos[0] - self.pos[0])-1
        ydif = abs(pchars[goto].pos[1] - self.pos[1]) -1
        if xdif+ydif == 0:
            self.pos[0] -= 1
            self.move()
            return True
        while xdif+ydif != 1 and movement > 0:
            print("{0} is moving".format(self.name))
            xdif = abs(pchars[goto].pos[0] - self.pos[0])
            ydif = abs(pchars[goto].pos[1] - self.pos[1]) 
            if xdif > ydif and xdif+ydif != 1:
                if char1.pos[0] - self.pos[0] > 0:
                    self.pos[0] += 1
                    movement -= 1
                    for char in chars:
                        if abs(char.pos[0] - self.pos[0]) + abs(char.pos[1] - self.pos[1]) == 0:
                            if enemy.name == self.name:
                                pass
                            else:
                                print("spawned at wrong point!")
                                self.pos[0] -= 1
                                movement = 0
                                battmap()
                else:
                    self.pos[0] -= 1
                    movement -= 1
                    battmap()
                            
            if ydif > xdif:
                if char1.pos[1] - self.pos[1] > 0:
                    self.pos[1] += 1
                    movement -= 1
                    for enemy in enemies:
                        if abs(enemy.pos[0] - self.pos[0]) + abs(enemy.pos[1] - self.pos[1]) == 0:
                            if enemy.name == self.name:
                                pass
                            else:
                                self.pos[1] -= 1
                                movement = 0
                                battmap()
                else:
                    self.pos[1] -= 1
                    movement -= 1
                    battmap()

            

    # find closest character
    # if multiple, go to one with most range
    #
    #
        
    def attack(self):
        count = 0
        options = []
        for char in pchars:
            if abs(char.pos[0]-self.pos[0]) + abs(char.pos[1]-self.pos[1]) <= self.attrnge:
                options.append(char)
                count += 1
                print(str(count)+ ":" + char.name)
        if count == 0:
            print("No targets for {0}!".format(self.name))
            return True
        if count > 1:
            optrnge = []
            print("selecting target")
            for option in options:
                optrnge.append(option.attrnge)
                target = min(optrnge)
                target = options[optrnge.index(target)]
                
        else:
            target = options[0]
        var = round(randint(0,1))
        direction = round(randint(-1,1))
        var = var*direction
        damage = self.damage + var
        target.hp -= damage
        print("{0} did {1} damage to {2}!".format(self.name,damage,target.name))
        print("{} ha been reduced to {} hp!".format(target.name,target.hp))
        if target.hp <= 0:
            print("{0} has died".format(target.name))
            chars.remove(target)
    # anyone in range?
    # if multiple, attack with longest range
    # death check
    #
    #
    #
    
    def turn(self):
        self.move()
        self.attack()
        
#main loop
print("welcome to the dungeon! you get three characters that you will lead to proseper or demise!")
print("")
print("there are 5 classes for you to choose form right now \n1:fighter \n2:barbarian \n3:wizard \n4:cleric \n5:sorcerer")
if input("would you like a description of all the roles?(y/n)\n>>>") == "y":
    print("The fighter specialises in doing damage, and has moderate Hp                      Hp:Med  Dmg:Hi    Mp:Non Support:L/N Rang:var  movment:fast")
    print("The barbarian foucuses on taking hits, while doing a decent amount of damage      Hp:Hi   Dmg:Med   Mp:L/N Support:M/L Range:1   movment:med")
    print("The wizard foucuses on damaging spells, with a few support spells                 Hp:Low  Dmg:Hi    Mp:Hi  Support:L/N Range:5 movment:slow")
    print("The cleric foucuses on support spells, with a few damaging spells                 Hp:Med  Dmg:Low   Mp:Hi  Support:Hi  Range:3 movment:med ")
    print("The sorcerer has a mix of both damaging and support spells                        Hp:Low  Dmg:Med   Mp:Hi  Support:Med Range:4 movment:slow")

name = "Barb"

print("you wil get three characters on this journey, now you will select them")
char1 = newchar(4,"first")
        

char2 = newchar(5,"second")


char3 = newchar(6,"third")

pchars = [char1,char2,char3]
#might make one arguement that sets the rest of the goblin to reduce some input
goblin1 = goblin(3,15,1,[2,4],1)
goblin2 = goblin(3,20,2,[4,4],3)
chars = [char1,char2,char3,goblin1,goblin2]
enemies = [goblin1,goblin2]
gameover = False
roundCt = 0
line(4)
while gameover == False:
    battmap()
    if char1.hp > 0:
        char1.turn()
        line(4)
    else:
        print("{0} is dead :(".format(char1.name))
    if char2.hp > 0:
        battmap()
        char2.turn()
        line(4)
    else:
        print("{0} is dead :(".format(char2.name))
    if char3.hp > 0:
        battmap()
        char3.turn()
        line(4)
    else:
        print("{0} is dead :(".format(char3.name))
    line(4)

    if len(enemies) == 0:
        if roundCt == 0:
            goblin3 = goblin(3,30,3,[9,4],1)
            enemies.append(goblin3)
            chars.append(goblin3)
            goblin4 = goblin(4,40,4,[9,5],3)
            enemies.append(goblin4)
            chars.append(goblin4)
            roundCt += 1
        elif roundCt == 1:
            goblin5 = goblin(5,50,5,[9,1],1)
            enemies.append(goblin5)
            chars.append(goblin5)
            goblin6 = goblin(6,60,6,[9,9],5)
            enemies.append(goblin6)
            chars.append(goblin6)
            roundCt += 1
        else:
            print("Game over, you have vanquished all of your foes!")
            gameover = True
    if len(pchars) == 0:
        print("You have lost, all your characters are dead :(")
        gameover = True
    for enemy in enemies:
        enemy.turn()
        line(4)
    input("move on?(enter)")
    line(32)

            
        

#psuedocode(?)
#start
#select character classes
#spawn enemies
#determin inititive
#  combat
#  run through init order
#  turn actions:
#      move
#      action(?)
      
