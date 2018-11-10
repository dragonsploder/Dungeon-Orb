# DO

import random
import time
import math

DMS = ["Kill", "Map", "Wait", "Anti-death"]

def Start():
    global Health
    global BHealth
    global Gold
    global GC
    global Loot1
    global ShopStuffOne
    global rooms
    global Dungeon
    global HO
    global Score
    global KV
    global slot1
    global slot2
    global slot3
    global slot4
    global PBuff
    global Ex
    global MRate
    global alive
    global EW
    global OP
    global MAP
    global AntiD
    global RN

    RN = False
    AntiD = False
    OP = 0
    EW = False
    alive = 0
    MRate = 0
    slot1 = "Punch"
    slot2 = "Punch"
    slot3 = "Punch"
    slot4 = "Confidence"
    PBuff = 0
    Ex = 0
    KV = False
    HO = False
    Health = 10
    BHealth = 10
    Gold = 0
    GC = False
    Score = 0

    MAP = {
        1: "              ",
        2: "              ",
        3: "              ",
        4: "              ",
        5: "              ",
        6: "              ",
        7: "              ",
        8: "              ",
        9: "              ",
        10: "              ",
        11: "              ",
        12: "              ",
        13: "              ",
        14: "              ",
        15: "              ",
        16: "              ",
        17: "              ",
        18: "              ",
        19: "              ",
        20: "              ",
        21: "              ",
        22: "              ",
        23: "              ",
        24: "              ",
        25: "              ",
    }

    Loot1 = {
        "Kick": "item",
        "Opportunity": "item",
        "Red Potion": "item",
        "Rusted Sword": "item",
        "Run Away": "item",
        "Ring": "item",
        "Cloak": "buff",
        "Ghost Ward": "buff",
        "Health Amulet": "buff"
    }

    ShopStuffOne = {}

    rooms = {
        1: "a Hall        ",
        2: "a Shop        ",
        3: "a Monster cave",
        4: "an Evil lair  ",
        5: "the Pit       ",
        6: "the Entrance  "
    }

    Dungeon = [2,2,2,3,4,5]

    print("------------------------------------------------------------------------------------------")
    print("Dungeon Orb")
    print("")

    CreateDungeon()
    SetShops1()
    Move()

def Slots():
    print("You have:")
    print(slot1,"(1) |",slot2,"(2) |",slot3,"(3) |",slot4,"(Buff)")

def CreateDungeon():
    i = 0
    while i < 18:
        Dungeon.append(random.choice([1,2,3,3]))
        i = i + 1
    random.shuffle(Dungeon)
    Dungeon.insert(0, 6)

def reset():
    global monsters1
    monsters1 = {
        "Disembodied Hand" : {"HP": 6,"AD": 2},
        "Troll" : {"HP": 4,"AD": 3},
        "Wolf": {"HP": 3,"AD": 4},
        "Orc": {"HP": 8, "AD": 1},
        "Ghost": {"HP": 2, "AD": 9},
        "Big Rat": {"HP": 2, "AD": 2}
        }

def TScore():
    global Score
    print("You scored:", Score)
    print("A name for you score:")
    name = input(">")
    t = name + "-" + str(Score) + "\n"
    f = open("DS.txt", "a")
    f.write(t)
    f.close()
    f = open("DS.txt", "r")
    contents = f.read()
    f.close()
    print("Here are others scores. Lower is better")
    print(contents)

def GM():
    reset()
    Ran = random.choice([1,2,3])
    if EW == True:
        Monster = random.choice(list(monsters1))
        while Monster == "Ghost":
            Monster = random.choice(list(monsters1))
    else:
        Monster = random.choice(list(monsters1))
    z = 1
    if Ran == 1:
        monsters1[Monster]["AD"] = monsters1[Monster]["AD"] + z
        monsters1[Monster]["HP"] = monsters1[Monster]["HP"] + z
    elif Ran == 2:
        monsters1[Monster]["AD"] = monsters1[Monster]["AD"] - z
        monsters1[Monster]["HP"] = monsters1[Monster]["HP"] - z
    return Monster

def SetShops1():
    global ShopStuffOne
    y = 0
    i = 0
    ShopStuffOne = {}
    while i < 3:
        if y == 25:
            y = 0
        if Dungeon[y] == 2 and random.choice([0,1,2]) == 1:
            item = random.choice(list(Loot1))
            ShopStuffOne[y] = item
            y = y + 1
            i = i + 1
        else:
            y = y + 1

def pMap():
    global MAP
    print("")
    print("--------------------------------------------------------------------------------------")
    print("|", MAP[0], "|", MAP[1], "|", MAP[2], "|", MAP[3], "|", MAP[4], "|" )
    print("--------------------------------------------------------------------------------------")
    print("|", MAP[5], "|", MAP[6], "|", MAP[7], "|", MAP[8], "|", MAP[9], "|" )
    print("--------------------------------------------------------------------------------------")
    print("|", MAP[10], "|", MAP[11], "|", MAP[12], "|", MAP[13], "|", MAP[14], "|" )
    print("--------------------------------------------------------------------------------------")
    print("|", MAP[15], "|", MAP[16], "|", MAP[17], "|", MAP[18], "|", MAP[19], "|" )
    print("--------------------------------------------------------------------------------------")
    print("|", MAP[20], "|", MAP[21], "|", MAP[22], "|", MAP[23], "|", MAP[24], "|" )
    print("--------------------------------------------------------------------------------------")
    print("")

def GOrb():
    global slot4
    global HO
    print("You take the orb off it's pedestal")
    slot4 = "Orb"
    HO = True

# Rooms

def Hall():
    global Health 
    global BHealth
    Health = Health + 2 
    if Health > BHealth:
        Health = BHealth
    print("")

def Shop():
    global Gold
    global x
    global slot1
    global slot2
    global slot3
    global slot4
    print("Your gold:", Gold)
    if x in ShopStuffOne and slot4 != "Orb":
        thing = ShopStuffOne[x]
        cost = 8
        print("You can buy:", thing,"for 8 gold")
        if Gold >= cost:
            if Loot1[thing] == "item":
                print("Select wich slot you want to exchange. If you don't want to, press 0")
                Slots()
                cmd = input(">")
                while cmd != "1" and cmd != "2" and cmd != "3" and cmd != "0":
                    print("You can't do that")
                    cmd = input(">")   
                if cmd == "3":
                    if slot3 != "Punch" and slot3 not in DMS:
                        del Loot1[slot3]
                    slot3 = thing
                    Gold = Gold - cost
                    SetShops1()
                elif cmd == "1":
                    if slot1 != "Punch" and slot1 not in DMS:
                        del Loot1[slot1]
                    slot1 = thing
                    Gold = Gold - cost
                    SetShops1()
                elif cmd == "2":
                    if slot2 != "Punch" and slot2 not in DMS:
                        del Loot1[slot2]
                    slot2 = thing
                    Gold = Gold - cost
                    SetShops1()
                else:
                    pass
            else:
                print("Press 4 to exchange. If you don't want to, press 0")
                Slots()
                cmd = input(">")
                while cmd != "4" and cmd != "0":
                    print("You can't do that")
                    cmd = input(">")   
                if cmd == "0":
                    pass
                else:
                    if slot4 != "Confidence" and slot4 not in DMS:
                        del Loot1[slot4]
                    slot4 = thing
                    Gold = Gold - cost
                    SetShops1()
                    CBuff()
        else:
            print("However you don't have enough gold to buy it")
    else:
        print("There is nothing to buy in this shop")
        print("")

def Monster():
    global Gold
    global Health
    global x
    global RN
    Monster = GM()
    print("You run into a:", Monster)
    al = monsters1[Monster]["HP"]
    dam = monsters1[Monster]["AD"]
    Fight(al, Monster, dam)
    if RN != True:
        Gold = Gold + dam
    else:
        RN = False
    print("")

def Lair():
    global KV
    if KV == False:
        print("Fight the Villan? y/n")
        cmd = input(">")
        while cmd != "y" and cmd != "n":
            print("You can't do that")
            cmd = input(">")
        if cmd == "y":
            print("")
            print("You enter the lair and hear a evil laugh. You prepare for battle")
            Fight(13, "The Villan", 2)
            KV = True
            GOrb()
    else:
        print("There is nothing left for you here.")
        
def Pit():
    global HO
    global GC
    if HO == True:
        print("Throw orb? y/n")
        cmd = input(">")
        while cmd != "y" and cmd != "n":
            print("You can't do that")
            cmd = input(">")
        if cmd == "y":
            print("You almost feel sad as you let go")
            HO = False
            GC = True
            CBuff()
    else:
        print("Jump into the empty abyss? y/n")
        cmd = input(">")
        while cmd != "y" and cmd != "n":
            print("You can't do that")
            cmd = input(">")
        if cmd == "y":
            PitGame()
        print("")

def Entrance():
    global GC
    global Health
    global Gold
    global x
    global Score
    global slot1
    global slot2
    global slot3
    global slot4
    print("Move On (0)")
    print("Exit Dungeon (1)")
    print("Drop Items (2)")
    print("Info (3)")
    print("Map (4)")
    print("Quit(5)")
    cmd = input(">")
    while cmd != "0" and cmd != "1" and cmd != "2" and cmd != "3" and cmd != "4" and cmd != "5":
            print("You can't do that")
            cmd = input(">")
    if cmd == "1" and GC == True:
        print("The People thank you, but inform you that you must continue")
        print("-----------------------------------------------------------")
        TScore()
        Start()
    elif cmd == "1" and GC == False:
        print("The People are upset that you did not follow there wishes.")
        Fight(1000, "The People", 1000)
        print("You defeat The People")
        print("A smile crosses your face")
        print("-------------------------")
        Start()
    elif cmd == "2":
        print("")
        print("You drop your items")
        print("")
        slot1 = "Punch"
        slot2 = "Punch"
        slot3 = "Punch"
        slot4 = "Confidence"
        Entrance()
    elif cmd == "3":
        print("""
You are in Dungeon. You must find the demon orb and throw it into the pit for The People.
The Orb is in The Villan's Lair.

To fight monsters use one of your three items.
You also have a buff slot which is always active.

Monsters give you gold to buy items in shops.
Every time you buy an item all shops will reset.

Halls increase your health.


A Text-Based Game by Joshua Bourgeot
        """)
        Entrance()
    elif cmd == "4":
        pMap()
        Entrance()
    elif cmd == "5":
        print("Are you sure? y/n")
        cmd = input(">")
        while cmd != "y" and cmd != "n":
            print("y/n")
            cmd = input(">")
        if cmd == "y":
            print("Bye")
            exit(1)
        print("Good choice")
        print("")
        Entrance()
    else:
        pass
    print("")

# Rooms

# items

def Punch():
    global alive
    global Ex
    alive = alive - (1 + Ex)
    Ex = 0

def Kick():
    global alive
    global Ex
    alive = alive - (random.choice([0,2]) + Ex)
    Ex = 0
    
def Opportunity():
    global OP
    global Ex
    if OP < 1:
        Ex = 2
        OP = OP + 1
    else:
        Ex = 1

def RedPotion():
    global Health
    Health = Health + 3
    if Health > BHealth:
        Health = BHealth
    else:
        pass

def RustedSword():
    global alive
    global Ex
    alive = alive - (2 + Ex)
    Ex = 0
    
def RunAway():
    global RN
    print("You run away")
    print("")
    RN = True

def Ring():
    global alive
    global Ex
    alive = alive - (random.choice([0,3]) + Ex)
    Ex = 0

def Kill():
    global alive
    global Ex
    alive -= alive
    Ex = 0

def Map():
    global Dungeon
    print("")
    print("---------------------")
    print("|", Dungeon[0], "|", Dungeon[1], "|", Dungeon[2], "|", Dungeon[3], "|", Dungeon[4], "|" )
    print("---------------------")
    print("|", Dungeon[5], "|", Dungeon[6], "|", Dungeon[7], "|", Dungeon[8], "|", Dungeon[9], "|" )
    print("---------------------")
    print("|", Dungeon[10], "|", Dungeon[11], "|", Dungeon[12], "|", Dungeon[13], "|", Dungeon[14], "|" )
    print("---------------------")
    print("|", Dungeon[15], "|", Dungeon[16], "|", Dungeon[17], "|", Dungeon[18], "|", Dungeon[19], "|" )
    print("---------------------")
    print("|", Dungeon[20], "|", Dungeon[21], "|", Dungeon[22], "|", Dungeon[23], "|", Dungeon[24], "|" )
    print("---------------------")
    print("")

# items

# buffs 

def Confidence():
    global PBuff
    PBuff = 0.5

def Cloak():
    global MRate
    MRate = 0.25

def GhostWard():
    global EW
    EW = True

def HealthAmulet():
    global BHealth
    BHealth = 13

def Orb():
    global BHealth
    global Health
    global Ex
    BHealth = 1000
    Health = BHealth
    Ex = 1000

def AntiDeath():
    global AntiD
    AntiD = True

# buffs

def item(slot):
    if slot == "Punch":
        Punch()
    elif slot == "Kick":
        Kick()
    elif slot == "Opportunity":
        Opportunity()
    elif slot == "Red Potion":
        RedPotion()
    elif slot == "Rusted Sword":
        RustedSword()
    elif slot == "Run Away":
        RunAway()
    elif slot == "Ring":
        Ring()
    elif slot == "Kill":
        Kill()
    elif slot == "Map":
        Map()
    else:
        pass
    
def Useitem(num):
    if num == "1":
        item(slot1)
    elif num == "2":
        item(slot2)
    else:
        item(slot3)

def Buff(b):
    if b == "Confidence":
        Confidence()
    elif b == "Cloak":
        Cloak()
    elif b == "Ghost Ward":
        GhostWard()
    elif b == "Health Amulet":
        HealthAmulet()
    elif b == "Orb":
        Orb()
    else:
        AntiDeath()

def CBuff():
    global PBuff
    global MRate
    global EW
    global BHealth
    global Health
    global Ex
    global AntiD
    AntiD = False
    BHealth = 10
    Health = BHealth
    Ex = 0
    BHealth = 10
    EW = False
    MRate = 0
    PBuff = 0

def DIW(x):
    if random.random() < x:
        return True
    else:
        return False

def MonAttack(AD):
    global Health
    global MRate
    AD = AD - PBuff
    if AD < 0:
        pass
    elif MRate == 0:
        Health = Health - AD
    else:
        if DIW(MRate) == False:
            Health = Health - AD

def Fight(Alive, Monst, MAD):
    global alive
    global Health
    global BHealth
    global OP
    global x
    global AntiD
    alive = Alive
    while alive > 0:
        if Health <= 0:
            if AntiD == True:
                print("Die? y/n")
                if input(">") == "n":
                    Health = BHealth
                else:
                    x = 0
                    Health = BHealth
                    OP = 0
                    Move()
            else:
                print("")
                print("-------")
                print("You die")
                print("-------")
                x = 0
                Health = BHealth
                OP = 0
                Move()
        Buff(slot4)
        print("You      |", Monst)
        print("HP = ", Health, "| HP = ", alive)
        Slots()
        cmd = input(">")
        while cmd != "1" and cmd != "2" and cmd != "3":
            print("You can't do that")
            cmd = input(">")
        Useitem(cmd)
        if alive > 0 and RN != True:
            MonAttack(MAD)
    if RN != True:
        print("")
        print("You defeated the", Monst)
        print("")
    OP = 0

def Move():
    global x
    global Score
    global MAP
    global slot1
    global slot2
    global slot3
    global slot4
    x = 0
    while x < 25:
        Number = Dungeon[x]
        room = rooms[Number]
        MAP[x] = room
        Score = Score + 1
        print("")
        print("You are in", room)
        if room == "a Hall        ":
            Hall()
        elif room == "a Shop        ":
            Shop()
        elif room == "a Monster cave":
            Monster()
        elif room == "an Evil lair  ":
            Lair()
        elif room == "the Pit       ":
            Pit()
        else:
            Entrance()
        if x == 0:
            print("You can go down(d) or right(r)")
            dirct = input(">")
            while dirct != "d" and dirct != "r" and dirct != "DM":
                print("You cant go there")
                dirct = input(">")
        elif x == 4:
            print("You can go down(d) or left(l)")
            dirct = input(">")
            while dirct != "d" and dirct != "l":
                print("You cant go there")
                dirct = input(">")
        elif x == 20:
            print("You can go up(u) or right(r)")
            dirct = input(">")
            while dirct != "u" and dirct != "r":
                print("You cant go there")
                dirct = input(">")
        elif x == 24:
            print("You can go up(u) or left(l)")
            dirct = input(">")
            while dirct != "u" and dirct != "l":
                print("You cant go there")
                dirct = input(">")
        elif x == 1 or x == 2 or x == 3:
            print("You can go down(d), left(l) or right(r)")
            dirct = input(">")
            while dirct != "d" and dirct != "l" and dirct != "r":
                print("You cant go there")
                dirct = input(">")
        elif x == 5 or x == 10 or x == 15:
            print("You can go down(d), up(u) or right(r)")
            dirct = input(">")
            while dirct != "d" and dirct != "u" and dirct != "r":
                print("You cant go there")
                dirct = input(">")
        elif x == 9 or x == 14 or x == 19:
            print("You can go down(d), up(u) or left(l)")
            dirct = input(">")
            while dirct != "d" and dirct != "u" and dirct != "l":
                print("You cant go there")
                dirct = input(">")
        elif x == 21 or x == 22 or x == 23:
            print("You can go left(l), right(r) or up(u)")
            dirct = input(">")
            while dirct != "l" and dirct != "r" and dirct != "u":
                print("You cant go there")
                dirct = input(">")
        else:
            print("You can go in any direction (r-l-d-u)")
            dirct = input(">")
            while dirct != "r" and dirct != "l" and dirct != "d" and dirct != "u":
                print("You cant go there")
                dirct = input(">")
        if dirct == "u":
            x = x - 5
        elif dirct == "d":
            x = x + 5
        elif dirct == "r":
            x = x + 1
        elif dirct == "DM":
            slot1 = "Kill"
            slot2 = "Map"
            slot3 = "Wait"
            slot4 = "Anti-Death"
            print("Entering DM")
        else:
            x = x - 1

# Minigame
def CheckNum():
    N = False
    while N == False:
        cmd = input("?>")
        try:
            cmd = int(cmd)
            N = True
        except ValueError:
            print("Numbers")
    return cmd

def PitGame():
    global x
    global Health
    global BHealth
    global OP
    global Gold
    hight = 500
    speed = 50
    magic = 100
    print("You find your self in the empty abyss.")
    print("To survive, you must slow your fall by shooting fire out of your hands")
    print("(Things are weird in the abyss)")
    print("")
    print("You can only have so much fire, so use it carefully")
    while True:
        hight = 500
        speed = 50
        magic = 100
        while hight > 0:
            print("Hight(ft):", str(hight) + "  Speed:", str(speed) + " f/s  " + "Magic:", str(magic))
            print("|" + " " * int(hight/10) + "*")
            if magic > 0:
                cmd = CheckNum()
                cmd = int(cmd)
                while cmd > magic:
                    print("Not enough magic")
                    cmd = CheckNum()
            else:
                cmd = 0
                time.sleep(0.5)
            speed -= cmd
            hight -= speed
            magic -= cmd
            if speed == 0:
                speed += 5
            else:
                speed += int(math.sqrt(abs(speed)))
        print("Hight(ft):0  ", "Impact Speed:", str(speed) + " f/s  " + "Magic:", str(magic))
        print("|" + " " * int(hight/10) + "*")
        if speed < 20:
            print("Great job")
            print("You find yourself back were you started, except now with more gold")
            Gold += 10
            x = 0
            Health = BHealth
            OP = 0
            Move()
        elif speed < 30:
            print("Just made it")
            print("You find yourself back were you started, except now with more gold")
            Gold += 10
            x = 0
            Health = BHealth
            OP = 0
            Move()
        elif speed > 100:
            print("Did you even try")
            x = 0
            Health = BHealth
            OP = 0
            Move()
        else:
            print("You died")
            x = 0
            Health = BHealth
            OP = 0
            Move()
# Minigame

Start()