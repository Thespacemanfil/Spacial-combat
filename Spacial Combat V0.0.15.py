import random
import time
import sys

#A game by Filip
#Spacial Combat first developed by Boredom Studios
#Enjoy the sphaget code and lack-luster gameplay

global shipname
global people
global shipaid
global alienaid
global torpedos
global score
global doge
global alienweak
global distance
global highscore
global display
global shield
global damage
global dmult
global laser
global torp
global beam
global repair
global newship
newship = False
repair = 0
beam = 300
torp = 0
laser = 15
damage = 0
shield = 0
display = "ERROR"
highscore = 0
alienweak = 0
dmult = 1
alienames = ['LAAT','X-Shaped fighter','Mon-Squid cruiser','Federation destroyer','Empire frigate','VORTEX','Death sphere','Death Sphere 2','Delapidated transport','Rag-tag pirate fleet']
aliename = random.choice(alienames)
shipaid = 1
alienaid = 0
people = 1
torpedos = 0
shipname = "Error"
val = 0
booler = True
score = 0
val2 = 0
doge = 10
distance = 1

def genship():
        global newship
        global shipaid
        global people
        global torpedos
        global score
        global distance
        global shield
        global dmult
        global doge
        global laser
        global torp
        global beam
        global repair
        newship = False
        repair = 0
        beam = 150
        torp = 0
        laser = 15
        doge = 10
        shield = 100 
        distance = random.randint(5000,20000)
        shipaid = random.randint(500,1000)
        people = random.randint(75,150)
        dmult = (people/100)
        torpedos = random.randint(9,15)
        score = 0
#Generates new ship stats at the beginning of the game and after death

def shipsname():
        global display
        global shipname
        global booler
        booler = True
        shipname = ("Error")
        while booler == True:
            shipname = input("\nThe name emblazened on the side of your ship is: ")
            if len(shipname) > 14: print("The side of your ship is too short to have that on it.\n")
            elif shipname == "": print("The ship had SOMETHING emblazened on its side, did it not?")
            else:
                booler = False
                display = shipname
                if (len(display) % 2) == 1: display = (display + "#")
                while len(display) < 14: display = ("~" + display + "~")
#Sets the name of the player's ship

def choice():
        select = 0
        global highscore
        global score
        if highscore < score: highscore = score
        print("--------------------------------------------------------------------------------------\n")
        print("")
        print("Welcome to")
        print(" ___________  ___  _____ _____  ___   _       _____ ________  _________  ___ _____") 
        print("/  ___| ___ \/ _ \/  __ \_   _|/ _ \ | |     /  __ \  _  |  \/  || ___ \/ _ \_   _|")
        print("\ `--.| |_/ / /_\ \ /  \/ | | / /_\ \| |     | /  \/ | | | .  . || |_/ / /_\ \| |")  
        print(" `--. \  __/|  _  | |     | | |  _  || |     | |   | | | | |\/| || ___ \  _  || |")  
        print("/\__/ / |   | | | | \__/\_| |_| | | || |____ | \__/\ \_/ / |  | || |_/ / | | || |")  
        print("\____/\_|   \_| |_/\____/\___/\_| |_/\_____/  \____/\___/\_|  |_/\____/\_| |_/\_/")  
        print("")
        print("The current highscore is",highscore,)
        print("")
        print("Press 1 to start")
        print("Press 2 to skip cutscene")
        print("Press 3 to exit the game")
        print("")
        print("--------------------------------------------------------------------------------------\n")
        genship()
        genalien()

        while select < 1 or select > 3:
                select = int(input("\nEnter your choice\n\n"))
                if select == 1: intro()
                elif select == 2:
                        shipsname()
                        time.sleep(2)
                        shipout()
                        time.sleep(2)
                        attack()
                elif select == 3: exit()
#Menu

def intro():
    global display
    print("")
    print("      SPACIAL COMBAT")
    time.sleep(2)
    print("")
    print("     +--------------+")
    print("    /|             /|")
    print("   / |            / |")
    print("  *--+-----------*  |")
    print("  |  |     .     |  |")
    print("  |  |   . o .   |  |")
    print("  |  |     .     |  |")
    print("  |  +-----------+--+")
    print("  | /            | /")
    print("  |/             |/")
    print("  *--------------*")
    print("")
    time.sleep(2)
    print("You have been tasked with transporting a speck of anti-matter to a site",distance,"Lm away\n")
    time.sleep(3)
    print("As the most accomplished pilot in the fleet, you were the obvious choice.\n")
    time.sleep(2)
    print("The fleet commander gives you an omega class cruiser with a worm drive for the mission. A single ship, as a fleet would attract too much attention")
    print("")
    time.sleep(1)
    shipsname()
    time.sleep(2)
    print("")
    print("                            ___________")
    print("                           |-----------|")
    print("           i               |===========|")
    print("           |               |,---------.|                      __--~\__--|")
    print("     ---,¬¬¬¬¬¬-_   `n     |`---------.|    `n    `n     ,--~~  __-/~~--|_____.")
    print("       |~~~~~~~~~|---~---/=|___________|=\---~-----~-----| .--~~  |  |__|     |")
    print("     -[|.--_. ===|~~~~~|-| |@@@@|+-+@@@| ",display," ||||___+_.  | `====.-.")
    print("     -[|.==~.    |~~~~~|-| |@@@@|+-+@@@| |]=~~~|\-++++-[| ||||~~~+~.  | .====.-;")
    print("       |_________|---u---\=|~~~~~~~~~~~|=/---u-----u-----| .--__  |  |~~|     |")
    print("        \       /=-   `    |,---------.|      `     `    `--__  ~~-\__--.~~~~~|")
    print("----=:===\     /           |`---------.|                      ~~--_/~~--|")
    print("      --<:\___/--          |===========|")
    print("                           |-----------|")
    print("                           |___________|")
    print("")
    time.sleep(3)
    print("")
    print("Was loaded up with torpedos, rechargeable lazer cells, replacement parts and",people,"crew members")
    print("")
    time.sleep(2)        
    print("Unfortunately, due to the value of the cargo, many are willing to have a go at you.")
    print("")
    time.sleep(2)
    print("Through the radar, you see plenty of ships scouting and scanning the area for you.")
    print("")
    time.sleep(2)
    print("One such enemy gets a little too close and detects you, jumping in immediately to attack.")
    print("")
    time.sleep(2)
    print("The",aliename,"fires some shots, shaking the crew into alertness.")
    attack()
#The full begininng of the game

def genalien():
    global aliename
    global alienaid
    global alienweak
    alienweak = 0
    aliename = (random.choice(alienames))
    alienaid = (random.randint(250,600))
#Creates a new alien
    
    
def alienout():
    if alienaid < 1: cruisingp()
    print("The enemy",aliename,"has",alienaid,"Health.\n")
#Checks if the alien is dead and reports status

def shipout():
    if shipaid < 1 or people < 1: defeat()    
    print("The",shipname,"has",shipaid,"Health, and",people,"crewmembers.")
    print("You also have",torpedos,"torpedos left and your shields are at",shield,"points\n")
#Checks if ship is dead and reports status

def dmgtaken(damage):
    global shipaid
    global shield
    if damage == 0: print("\nThe attack misses completely.\n")
    elif shield == 0:
            print("The attack passes straight through your chargeless shield.")
            time.sleep(2)
            defendcon()
    elif damage > shield:
                  damage -= shield
                  print("\nYour shield absorbs",shield,"damage and runs out of charge.")
                  shield = 0
                  shipaid -= damage
                  print("Your ship takes",damage,"damage and lets the blast through the shields.\n")
                  time.sleep(2)
                  print("")
                  print("    ___+ # ~ +")
                  print("   /    + ~ # ' @")
                  print("   | -0-> |  #")
                  print("   \______/")
                  print("")
                  time.sleep(2)
                  defendcon()
    else:
                  shield -= damage
                  print("\nYour shield absorbs",damage,"damage and now has",shield,"charge.\n")
                  time.sleep(2)
                  print("    ______")
                  print("   /      \\")
                  print("   | -0-> |")
                  print("   \______/")
                  print("")
                  time.sleep(2)
    if shipaid < 1 or people < 1: defeat()
#Takes damage away from shields before main health



def defend():
    global shipname
    global people
    global shipaid
    global alienaid
    global torpedos
    global score
    global doge
    val = random.randint(1,doge)
    if val < 4:
        damage = (random.randint(25,90))
        print("The enemy",aliename,"fired its rotary laser.")
        dmgtaken(damage)
        time.sleep(2)
    elif val < 7:
        damage = ((random.randint(50,75)) * (random.randint(0,3)))
        print("The",aliename," fired its missiles and")
        dmgtaken(damage)
        time.sleep(2)
    elif val == 8:
        damage = (random.randint(50,300))
        print("The",aliename,"fired its centre cannon,")
        dmgtaken(damage)
        time.sleep(2)

        if alienaid < 1:
                print("But destroyed itself in the process")
                cruisingp()
        else:
                print("And survived the damage its center cannon caused it")

    elif shipaid < 50:
        print("The crew of the",aliename,"see how damaged your ship is, and pity you. They leave.")
        cruisingp()

    else:
            print("The",aliename,"fired but completely missed your ship.")
            score += 25

    if shipaid < 0:
        defeat()
    else:
        score += 50
        time.sleep(2)
        shipout()
        attack()
#Alien's attack cycle
 
def attack():
     global repair
     global laser
     global torp
     global beam
     global shipname
     global people
     global shipaid
     global torpedos
     global alienaid
     global score
     global dmult
     global doge
     global distance
     dmult = (people/100)
     select = 'error'
     val = 0
     damage = 0
     alienout()

     print("The",shipname,"lumbers into attack position, ready to fire any of the available weaponry.\n")
     time.sleep(2)
     print("It is equipped with varied damage but infinite -lazers-,")
     time.sleep(1)
     if torpedos > 2:
             time.sleep(1)
             print("Innacurate and limited but powerful -torpedos-,")
             time.sleep(1)
     print("an immensly powerful but self damaging -ion beam-,")
     time.sleep(2)
     print("or we could fire the -engines- to gain distance to better evade enemy attacks.\n")
     time.sleep(1)
     select = input("Which weapon contained within the hyphens do you want to fire?\n")

     if 'la' in select:
             if alienweak == 1: dmult += 0.2
             damage = (round(dmult * random.randint(5,laser) * random.randint(5,15)))
             if damage < 1: damage = random.randint(10,50)
             alienaid -= damage
             dmult -= 0.2
             score += 5
             print("The gun spools up and glowing red lasers fly out, melting holes in the enemy",aliename,", dealing",damage,"damage.")
             
     elif 'to' in select:
             if torpedos < 3:
                 print("Not enough torpedos to perform a launch.")
                 score -= 10
             else:
                 if alienweak == 2: dmult += 0.2
                 print("The long cylinders slide out of their launch tubes,") 
                 torpedos -= 3
                 time.sleep(2)
                 damage = round(random.randint(torp,3) * random.randint(75,125) * dmult)
                 if damage < 1: damage = random.randint(50,100)
                 alienaid -= damage
                 if damage > 0: print("and detonate once inside the enemy",aliename,", dealing",damage,"damage.")
                 else: print("They miss.")
                 dmult -= 0.2
                 time.sleep(2)
                 print("You have",torpedos,"torpedos left")
                 score += 15
                
     elif 'ion' in select:
                 if alienweak == 3: dmult += 0.2
                 time.sleep(2)
                 print("The reactor, vital to keeping your ship online, heats up and releases more power than it is rated for.")
                 damage = round(random.randint(150,300) * dmult)
                 if damage < 1: damage = random.randint(100,250)
                 alienaid -= damage
                 dmult -= 0.2
                 shipaid -= (random.randint(beam,200))
                 time.sleep(2)
                 if shipaid < 0:
                     time.sleep(6)
                     print("Your crew begin to hear a creaking, before being incinerated by the fireball expanding outwards from the generator room.")
                     defeat()
                 else:
                     val = (random.randint(1,6))
                     if val < 5:
                             print("The",shipname,"survives the core overheat, though scorch marks are visible in the chamber.")
                             time.sleep(2)
                             shipout()
                             score += 25
                             print("\nThe attack deals",damage,"damage to the",aliename)
                     else:
                             print("The",shipname,"survives the core blast, though the brain of a crew member is found slumped in the chamber,")
                             people -= 1
                             dmult -= 0.01
                             time.sleep(3)
                             print("")
                             print("       .__---~~~(~~-_.")
                             print("   _-.  ) -~~- ) _-; )_")
                             print("  (  ( `-,_..`.,_--_ ;_,)_")
                             print(" (  -_)  ( -_-~  -_ `,    )")
                             print(" (_ -_ _-~-__-~`, ,; )__-;))--___--~~~--__--~~--___--__..")
                             print(" _ ~`_-;( (____;--==,,_))))--___--~~~--__--~~--__----~~~;`=__-~+_-_.")
                             print("(@) (@) `````      `-_(())_-~  mn")
                             print("")
                             time.sleep(3)
                             print("their skull stopped the plasma from instantly evaporating it.")
                             time.sleep(3)
                             print("Using a dna test you manage to identify their remains and contact their kin.")
                             time.sleep(4)
                             print("\nThe attack deals",damage,"damage to the",aliename)
                             score -= 40
                             shipout()
     elif 'eng' in select:
             doge += 3
             distance -= 50
             score += 10
             time.sleep(2)
             print("The",shipname,"fires its engines and pulls away, making it a harder target to hit.")
             time.sleep(2)        
     else:
              print("You chose not to fire. Next time give a choice.\n")
              score -= 10

     if alienaid < 1:
         score += 10
         time.sleep(5)
         enemyexplosion()
         select = input("Should we scavenge the wreck for ship upgrades and resources? It would mean being spotted by enemy ships.\n")
         if "y" in select:
                 scavenge()
                 doge = 10
                 prenemy() 
         else:
                 print("you decide not to, instead evading detection.")
                 shipaid += repair
                 time.sleep(3)
                 print("The",shipname,"slips out of enemy sensor range in the confusion and rubble.")
                 doge = 10
                 time.sleep(5)
                 cruisingp()
     elif alienaid < 25:
         time.sleep(3)
         val = random.randint(1,4)
         if val = 1:
                 print("The damaged enemy",aliename,"fires its thrusters and escapes, their ship too damaged to continue fighting.")         
                 time.sleep(3)
                 doge = 10
                 print("Before you can even react, another enemy ship swoops in and hits your ship in a suprise attack")
                 time.sleep(1)
                 genalien()
                 blownengines()
                 time.sleep(3)
                 defend()
         if val = 2:
                 print("The",aliename,"ship rams into you as a final act of defiance.")
                 damage = ((random.randint(0,20))*alienaid)
                 time.sleep(3)
                 dmgtaken(damage)
                 time.sleep(2)
                 print("The large explosion puts you on the radar of an enemy ship.")
                 time.sleep(2)
                 prenemy()
         if val = 3:
                 print("The enemy ship surrenders, and their remaining crew members offer themselves up as slaves.")
                 val = random.randint(2,20)
                 print(val,"people come aboard.")
                 people += val
                 cruisingp()
         if val = 4:
                 print("The",aliename,"ship is on its last legs, and you cannot resist taking a shot.")
                 time.sleep(4)
                 enemyexplosion():
                 print("The large explosion puts you on the radar of an enemy ship.")
                 time.sleep(2)
                 prenemy()
     else:
         alienout()
         time.sleep(4)
         defend()
#Player's attack cycle

def defendcon():
     global shipname
     global display
     global shipaid
     global score
     global people
     global torpedos
     select = (random.randint(3,6))
     if select == 3:
            select = (random.randint(1,6))
            damage = (random.randint(1,3))
            torpedos -= select
            people -= damage
            print("The attack sailed into the torpedo bay, destroying",select,"torpedos, and killing",damage,"people")
            damage = (random.randint(10,50))
            shipaid -= damage
            print("The",aliename,"'s attack detonated the torpedos, causing an explosion dealing",damage,"damage.")
     elif select == 4:
            damage = (random.randint(1,2))
            people -= damage
            print("The attack hit one of your turbo lazers, killing",damage,"crew")
            damage = (random.randint(10,30))
            shipaid -= damage
            print("and causing",damage,"damage to the",shipname,".\n")
     elif select == 5:
             damage = random.randint(20,100)
             shipaid -= damage
             print("The attack slammed into the core reactor, dealing the",shipname,"",damage,"more damage")
     elif select == 6:
             damage = random.randint(20,80)
             shipaid -= damage
             print("The blast scorched a structual beam, doing",damage,"damage.")
     time.sleep(3)
     blownring()

def scavenge():
        global shipname
        global torpedos
        global repair
        global laser
        global torp
        global beam
        global people
        print("You decide to risk being detected to search the wreck.")
        time.sleep(2)
        select = random.randint(0,20)
        if select < 5:
                print("You find some torpedos floating around.")
                torpedos += random.randint(1,6)
                time.sleep(2)
        elif select < 7:
                print("You find some functioning repair robots. They are fragile so cannot be enabled during battle.")
                time.sleep(2)
                print("You program them to repair after each battle.")
                repair += 150
                time.sleep(2)
        elif select < 10:
                print("You find some components belonging to a lazer turret, and use them to upgrade your system.")
                laser += 10
                time.sleep(2)
        elif select < 13:
                if torp > 3:
                        torp = 3
                        print("You find a new torpedo launch tube, but it is a worse model than your current one.")
                        time.sleep(2)
                        print("At least you find a torpedo inside it.")
                        torpedos += 1
                else:
                        print("You find a new torpedo launch tube, increasing torpedo accuracy.")
                        torp += 1
                time.sleep(2)
        elif select < 14:
                print("You find some extra control rods that will reduce instability in the reactor while firing.")
                beam -= 25
                time.sleep(2)
        elif select < 17:
                val = random.randint(1,9)
                print("Your scanners detect a damaged escape pod with living inhabitants.")
                time.sleep(2)
                print("You dock with the ship, your crew with their weapons raised. Inside the pod you spot",val,"people.")
                time.sleep(2)
                print("Reluctantly, they come out of the escape pod. They plead for their lives, claiming they were prisoners on board the ship.")
                time.sleep(2)
                select = input("Do you leave them to -die- or take them -onboard-?\n")
                if "die" in select: print("You force them back in their pod and leave.")
                elif "on" in select:
                        print("You welcome them onto your ship. However the question arises-")
                        time.sleep(2)
                        select = input("Do you force them to be -crew-, or -drop- them off at the next planet?\n")
                        time.sleep(2)
                        if "cr" in select:
                                select = random.randint(1,3)
                                if select == 1:
                                        print("They don't take kindly to your decision. While passing a space station,")
                                        time.sleep(2)
                                        print("They steal a landing craft and fire a few shots at the",shipname,"before flying away.")
                                        shipaid -= random.randint(10,50)
                                        time.sleep(2)
                                        shipout()
                                else:
                                        people += val
                                        print("You gain",val,"crew.")
                                time.sleep(2)
                        elif "dr" in select: print("You drop them off at a fairly civilised planet.")
                else: print("You hesitate. The inhabitants take that a a signal to attack, and your crew fire upon them.")
        else:
                time.sleep(2)
                print("Your search comes up empty.")
                time.sleep(4)

        
def cruisingp():
        global distance
        global alienweak
        global score
        global shipname
        global shipaid
        global torpedos
        global people
        global shield
        global shields
        score += 100
        distance = distance - (random.randint(500,1000))
        if distance < 1:
                print("")
                print("As your ship coasts along, you come upon the delivery site.")
                time.sleep(3)
                ending()
        print("\nThe",shipname,"cruises out of range of enemy sensors. The shields recharge, the ship is patched up,")
        print("the crew spends some time building some torpedos, and you gain some new crew members.")
        if people > 200: people -= random.randint(5,20);print("Your ship becomes overcrowded, people die due to the lack of resources and accomodation.")
        if shield < 100: shield = 100
        else: shield += 50
        if shipaid < 250: shipaid = 250
        else: shipaid += 75
        torpedos += random.randint(1,3)
        people += random.randint(1,2)
        time.sleep(5)
        print("")
        print("All is quiet and peaceful...")
        print("")
        time.sleep(5)
        val = random.randint(0,10)
        if val == 0: print("and it stays that way.");time.sleep(5);cruisingp()
        elif val < 3:
                print("Your unaware crew leave the bridge unmanned for a little too long...")
                time.sleep(5)
                print("And you find that you have entered an asteroid field.")
                time.sleep(5)
                damage = random.randint(50,125)
                shipaid -= damage
                print("")
                print("A barrage of rocks strike your shield-less ship, doing",damage,"damage to your ship.")
                time.sleep(2)
                shipout()
                time.sleep(2)
                print("After a stern warning, you continue flying, albeit more carefully.")
                time.sleep(2)
                cruisingd()
        elif val < 5:
                print("You come upon a questionable trader offering a great deal.")
                time.sleep(2)
                print("Several of its highly skilled crew for a few torpedos.")
                time.sleep(2)
                choicer = input("Do we say yes to the deal captain?\n")
                if "yes" in choicer:
                        if torpedos == 0:
                                damage = random.randint(5,20)
                                print("You do not have any torpedos, the promised crew arrive and slaughter",damage,"of yours before you kill them.")
                                people -= damage
                                time.sleep(2)
                                print("You fire your lazers and destroy the trader.")
                                select = input("Should we scavenge the remains?")
                                if "y" in select: scavenge()
                                cruisingd()
                        elif torpedos < 3: torpedos = 0
                        else: torpedos -= 3
                        
                        if random.randint(1,3) == 1:
                                print("The trader does not send any crew,instead firing the torpedos you gave it at you.")
                                damage = ((random.randint(50,100)) * (random.randint(0,3)))
                                damagetaken(damage)
                                genalien()
                                time.sleep(2)
                                print("It reveals itself as an enemy",aliename)
                                time.sleep(2)
                                defend()
                        else:
                                val = random.randint(5,15)
                                people += val
                                print("The trader keeps its word and sends you",val,"crew in exchange for the few torpedos you send it.")
                                time.sleep(2)
                                cruisingp()
                else:
                        print("You don't trust the trader, and decide to fly away. You wonder what could have happened.")
                        cruisingp()
        elif val < 7:
                print("You come upon a comet, trailed by blue rocks. unable to scan them, you bring them inside.")
                time.sleep(2)
                print("You find they are hunks of neutionium, an unstable and radioactive element.")
                time.sleep(2)
                print("They would serve as a powerful fuel, but they decay quickly so would have to be used immediately.")
                time.sleep(2)
                print("Their radioactivity blocks all sensors, meaning if you were to use them you would have no idea if you were going in the right direction.")
                time.sleep(2)
                choicer = input("Dare risk using them?\n")
                if "yes" in choicer:
                        if random.randint(1,3) == 1:
                                val = random.randint(100,750)
                                distance += val
                                print("Your ship warps",val,"lm off course.")
                                time.sleep(2)
                                cruisingd()
                        else:
                                val = random.randint(500,2000)
                                distance -= val
                                print("Your disorientated ship warps",val,"lm towards the site.")
                                time.sleep(2)
                                cruisingp()
                else: print("You decide to safely drift out of the nebula.");time.sleep(2);cruisingp()
        else:
                prenemy()
                        
        
def cruisingd():
        global distance
        global alienweak
        global score
        global shipname
        global shipaid
        global torpedos
        global people
        global shield
        score += 100
        distance = distance - (random.randint(500,1000))
        if distance < 1:
                print("As you carefully cruise, you come upon the goal.")
                time.sleep(3)
                ending()
        print("The previous incident leaves your ship vunerable, enemies having your approximate location")
        prenemy()
            
    
def prenemy():
     global doge
     global distance
     global alienweak
     global score
     global shipname
     global shipaid
     global torpedos
     global people
     global shield
     global dmult
     dmult = dmult * (people/100)
     distance = distance - (random.randint(100,750))
     if distance < 1:
             ending()

     print("")
     print("------------------------------------------------------------------")
     print("")
     alienweak = 0
     print("Your sensors pick up an enemy vessel approaching. The ship's computer alerts you to some extra available power to help prepare for the attack.")
     time.sleep(3)
     genalien()
     print("The extra power can be diverted to the -lazers- to deal damage to the nearest enemy, -repair- the ship with our drones,")
     print("-scanners- to find a weakness in the next enemy, the -engines- to make progress and avoid the enemy, or -recharge- the shields.")
     select = str(input("Input the system power diversion request.\n\n"))
                         
     if "sniper" in select:
            alienaid = alienaid - round(random.randint(50,125) * dmult)
            check()
            print("The ",aliename," is struck by a streak of red, melting a small hole into it. It's health is lowered to ",alienaid)
     elif "repair" in select:
            shipaid = shipaid + (random.randint(50,150))
            print("The ",shipname," has been patched up somewhat to ",shipaid)
     elif "scan" in select:
            alienweak = random.randint(1,3)
            if alienweak == 1:
                select = "Lasers"
            elif alienweak == 2:
                select = "Torpedos"
            elif alienweak == 3:
                select = "ion beams"
            print("The alien ship is weak to",select)  
                
     elif "engine" in select:
            distance = distance - 500
            print("You move 500Lm closer")
            score += 20
            if distance < 0:
                    ending()
            val = random.randint(1,2)
            if val == 1:
                     print("You move far enough away that the enemy loses track of your ship.")
                     distance = distance - (random.randint(100,400))
                     print("A freindly ship manages to rendevous with you, restocking your ship.")
                     (time.sleep(2))
                     print("Torpedos, health and crew recived")
                     shipaid += 200
                     people += 20
                     torpedos += 12
                     score += 75
                     time.sleep(2)
                     if distance < 25:
                             print("While flying along with the freindly ship, you see your destination.")
                             ending()
                     print("The freindly ship spots an enemy ship, and fires a couple shots, distracting it enough to allow you to get into combat position.")
                     print("")
                     print("------------------------------------------------------------------\n")
                     print("")
                     attack()
            else:
                     blownengines()  
                     print("The enemy hit your engines with a red beam, your ship turned away from it trying to get away.")
                     shipaid = shipaid - (random.randint(5,75))
                     doge += 1
                     shipout()
                     print("")
                     print("------------------------------------------------------------------\n")
                     print("")
                     time.sleep(2)
                     defend()
     elif 'charge' in select:
            if shield < 25: shield += 100
            elif shield > 175: shield = 250 ; print("Shields at max.")
            else: shield += 75
            print("Shields have been charged to",shield)

     shield += 5                            
     print("")
     print("------------------------------------------------------------------\n")
     print("")
     attack()   
#Preperation stage for the next alien
  

def defeat():
     global newship
     global shipname
     global shipaid
     global score
     global display
     val = 0
     print("The",shipname,"goes up, the damage sustained being too high for the frame and core to handle, resulting in a catostrophic faliure.")
     if shipaid > -40:
         print("But thankfully, you and your crew managed to escape the ",shipname," with the anti-matter before it went up with a small bang.")
         time.sleep(2)
         print("")
         print("____    //===============\\")
         print("(o) \--//                 \\")
         print("<=====||   O  O  O  O  O   ))")
         print("(o) /--\\                 //")
         print("¬¬¬¬    \\===============//")
         print("")
         time.sleep(2)
         val = (random.randint(1,5))            
         if val < 4:
             score += 75
             print("A freindly ship locates your escape pods and takes you back to a nearby planet where you manage to find a replacement ship.")
             genship()
             time.sleep(2)
             print("")
             print("        _____")
             print("    ,-:` \;;,`;-,") 
             print("  .;-;_,;  ;:-;_,;.")
             print(" /;   ;/    ,  _`.-\\")
             print("| ;`. (`     /` ` \`|")
             print("|:.  `\`-.   \_   / |")
             print("|     (   `,  .`\ ;;|")
             print(" \     | .;     `-;/")
             print("  `.   ;/       _.;")
             print("    `;-._____.-;")
             print("")  
             time.sleep(4)
             shipname = (shipname + " 2")
             display = shipname
             while len(display) < 14: display = ("~" + display + "~")
             newship = True
             print("As you take off in your new ship, filled with fresh supplies and hired crew members, you are hit by a shot from an unfreindly ship.")
             genalien()
             time.sleep(2)
             defend()
         else:
                time.sleep(2)
                print("Unfortunetly, nobody finds you. You starve to death trapped in a small, steel coffin.")
                score =- 60
                print("Your score was ",score,"\n")
                choice()
     else:
         time.sleep(3)
         print("")
         print("                               ________________")
         print("                          ____/ (  (    )   )  \___")
         print("                         /( (  (  )   _    ))  )   )\\")
         print("                       ((     (   )(    )  )   (   )  )")
         print("                     ((/  ( _(   )   (   _) ) (  _____==~~~~n'_________")
         print("                    ( (  ( (_)   ((    (   )  .((_ ",display,">:|")
         print("                   ( (  )    (      (  )    )   ) . ) (----------")
         print("                  (  (   (  (   ) (~  _  ( _) ).  ) . ) ) ( )~~")
         print("                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )")
         print("                 ( (  ( \ ) (    (_  ( ) ( )  )   )~ )  )) ( )")
         print("                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )")
         print("                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )")
         print("                  ((  (   )(    (     _    )   _) _(_ (  (_ )")
         print("                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)")
         print("                   ((__)        \\||lll|l||///          \_))")
         print("                            (   /(/ (  )  ) )\   )")
         print("                          (    ( ( ( | | ) ) )\   )")
         print("                           (   /(| / ( )) ) ) )) )")
         print("                         (     ( ((((_(|)_)))))     )")
         print("                          (      ||\(|(|)|/||     )")
         print("                        (        |(||(||)||||        )")
         print("                          (     //|/l|||)|\\ \     )")
         print("                        (/ / //  /|//||||\\  \ \  \ _)")
         print("-------------------------------------------------------------------------------")
         print("You and your crew went down with the",shipname,"as the reactor detonated, destroying the artifact and wiping out the enemy ship with you.")
         time.sleep(5)
         score -= 75
         time.sleep(2)
         print("Your score was",score,"\n")
         time.sleep(2)
         choice()
#Player loss

def ending():
     global score
     global shipaid
     global torpedos
     global crew
     print("You finally arrive at the centurion storage facility, it's ion guns cover your landing and fend off any other attempts to attack.")
     time.sleep(2)
     print("")
     print("      ___________________")
     print("     /         \         \\")
     print("    / CENTURION \_________\\                                                ")
     print("   | =    =   =  | =  =  = |                                                ")
     print("   |   SECURE    |         |                                                ")
     print("   | =    =   =  | =  =  = |                            __________          ")
     print("   |   STORAGE   |         |               _____     __/        \ \         ")
     print("   | =    =   =  | =  =  = |              /     \___/    o  o  <(00)        ")
     print("   |  FACILITY   |         |       _      HHHH   _____   o  o  <(00)        ")
     print("   | =    =   =  | =  =  = |   ___ 0\     \_____/     \_________/_/        ")
     print("   |      ||     |         |   |.|-|        _||_     _/   _||_||_           ")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("")
     score += 1000
     time.sleep(2)
     print("You are celebrated on your home planet, for now the anti-matter can power the super weapon,")
     print("capable of destroying any planets standing in the way of the galactic empire. Rebel fighters and governments were making desperate attempts to stop you.")
     time.sleep(2)
     print("Your score was",score,"\n")
     choice()

def enemyexplosion():
         print("")
         print("----------------------------------------------------------------------")
         print("")
         print("                             ____")
         print("                     __,-~~/~    `---.")
         print("                   _/_,---(      ,    )")
         print("               __ /        <    /   )  \___")
         print("- ------===;;;====------------------===;;;===----- -  -")
         print("                  \/  ~~~~~~\~~)~/~~~~~~/")
         print("                  (_ (   \  (     >    \)")
         print("                   \_( _ <         >_>")
         print("                      ~ `-i i ::>|--")
         print("                          I;|.|.|")
         print("                         <|i::|i|`.")
         print("                        (` ^.;`-. ;)")
         print("----------------------------------------------------------------------")
         print("A spectacular lightshow occurs as the enemy",aliename,"disintegrates. ")
         print("----------------------------------------------------------------------")
         print("")

def blownengines():
                     time.sleep(3)
                     print("")
                     print("           @                ___________")
                     print("                   *       |-----------|")
                     print("    @      i               |===========|")
                     print("           |     !         |,---------.|                      __--~\__--|")
                     print("   ~ ---,¬¬¬¬£¬-_   `n     |`---------.|    `n    `n     ,--~~  __-/~~--|_____.")
                     print(" .    *   ~~~%~~~|---~---/=|___________|=\---~-----~-----| .--~~  |  |__|     |")
                     print("      .    &   |-+_. ===|~~~~~|-| |@@@@|+-+@@@| ",display," ||||___+_.  | `====.-.")
                     print("    ==~.@   ~   $  |~~~~~|-| |@@@@|+-+@@@| |]=~~~|\-++++-[| ||||~~~+~.  | .====.-;")
                     print("   }   |__(_=___+|---u---\=|~~~~~~~~~~~|=/---u-----u-----| .--__  |  |~~|     |")
                     print("        *       /=-   `    |,---------.|      `     `    `--__  ~~-\__--.~~~~~|")
                     print("---)=:===\   H /           |`---------.|                      ~~--_/~~--|")
                     print("      --<:\___/--          |===========|")
                     print("                           |-----------|")
                     print("                           |___________|")
                     print("")
                     time.sleep(3)

def blownring():
     print("")
     print("                            _____  ~ :")
     print("                           |----/   . >  @")
     print("           i               |===| ;   -    ,")
     print("           |               |,---.  0   |    .                 __--~\__--|")
     print("     ---,¬¬¬¬¬¬-_   `n     |`-----l ___    @             ,--~~  __-/~~--|_____.")
     print("       |~~~~~~~~~|---~---/=|___________|=\---~-----~-----| .--~~  |  |__|     |")
     print("     -[|.--_. ===|~~~~~|-| |@@@@|+-+@@@| ",display," ||||___+_.  | `====.-.")
     print("     -[|.==~.    |~~~~~|-| |@@@@|+-+@@@| |]=~~~|\-++++-[| ||||~~~+~.  | .====.-;")
     print("       |_________|---u---\=|~~~~~~~~~~~|=/---u-----u-----| .--__  |  |~~|     |")
     print("        \       /=-   `    |,---------.|      `     `    `--__  ~~-\__--.~~~~~|")
     print("----=:===\     /           |`---------.|                      ~~--_/~~--|")
     print("      --<:\___/--          |===========|")
     print("                           |-----------|")
     print("                           |___________|")
     print("")
     time.sleep(3)

         
choice()
