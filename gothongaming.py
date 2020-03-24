from sys import exit
from random import randint

class Scene(object):
    def enter(self): #when you call function enter, it prints some stuff out
        print("This scene is not yet configured. Subclass it and implement enter().")
        #exit(1)



class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map   #IT INITAILISES USING THE MAP OBJECT; MAP OBJECT HAS START-SCENE AS CENTRAL CORRIDOR
                                    #NOW THE ENGINE HAS A VARIABLE SCENE-MAP DEFINED AS CENTRAL CORRIDOR

    def play(self):                 #when you call play(), it sets the current_scene to opening_scene
        current_scene = self.scene_map.opening_scene()   #WHICH IS THE VARIABLE CENTRAL-CORRIDOR
        while True:
            print("\n-------------------")
            next_scene_name = current_scene.enter()
            print("You are currently in %s" % next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)




class Death():
    quips = [
         "You died. You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this.",
         "Looks like you just got thrown under a bus, literally",
         "My niece is better at this than you, and she's not even conceived yet",
         "Mum says it's my turn on the XBOX",
         "It's past your bedtime kiddo"
    ]
    def enter(self):  # when you call function enter, it prints some stuff out
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor():
    def enter(self):
        print("I finally wake after days of what seemed like a coma. I look in the small puddles on the floor")
        print("which showed my long brown hair and tired blue eyes.")
        print("You see a message pinned to the wall:")
        print("\n")
        print("The Gothons of Planet Nectune have invaded your transport ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armoury")
        print("put it in the bridge, and blow up after getting into an escape pod")
        print("\n")
        print("You're running down the central corridor to the Weapons Armoury when")
        print(" you hear the beeping from your heat detector. It keeps getting louder")
        print("and LOUDER until you suddenly  see these beedy red eyes staring right back at you.")
        print("Oh Shit !")
        print("A slime covered Gothon with red scaly skin and black teeth is now blocking the door to the armoury")
        print("\n")
        action=input("You're tired and drained, what do you do? > run away / fight / distract > ?")

        if action == "run away":
            print("You decide to run away. Good idea! Maybe.  You start the long marathon of the run back down the ")
            print("Central corridor. You try everything but your knees are getting weaker feeling that breath down your spine")
            print("Everything seems to be a blur whilst you run down this never ending corridor")
            print("Suddenly you feel a crunch in your foot followed by a pain in your knees")
            print("You fell.")
            print("That breathing down your spine increases by the second, as does your anxiety")
            print("You feel only numbness and realise that the spreading pool of blood is actually from you.")
            print("You get the hit of pain, followed by the hit of blankness.")
            return "death"
        elif action== "fight":
            print("You decide to against your instinct to fight the Gothon. You use your tremendous will power")
            print("and your puny strength.  With super human strength you rip off a pipe from the space ship wall")
            print("and with great effort you strike the Gothon on its slimy grimy red scaly head.")
            print("Alas! The Gothon does not even blink. As you try to strike again you see a blur of claw")
            print("as it swipes towards you and rips off your head!")
            return "death"
        elif action== "distract":     #THIS IS HOW TO PROCEED PAST THIS SCENE
            print("You decide to distract the Gothon. ")
            print("I've got nothing on me. And I'm too weak to fight or run.")
            print("I reach to you my trousers in which surprisingly I feel a metal box attached to my belt")
            print("Oh yes - the heat detector! ")
            print("I rip it off my belt not realising how vital the heat detector is for my mission.")
            print("I'm so tired and almost in a drunken state at this point.")
            print("As I panic, I press the button to make it beep extremely loudly; I throw the device across the ")
            print("corridor and into an isolation room.")
            print("I look up and see the beady reds eyes no longer staring at me.  The Gothon has gone into the Isolation room!")
            print("I sigh with relief and head into the armoury")
            print("SUCCESS!")
            return "laser_weapon_armory"

        else:
            print("You twat, can you not even type properly??! Unfortunately, your hesitation has not helped")
            print("The Gothon seizes its chance and splits you in half!")

        print("")


        return "death"

class LaserWeaponArmory():
    def enter(self):  # when you call function enter, it prints some stuff out
        print("You are now in the laser weapon armory")
        print("You enter the dark room of the weapon armoury")
        print("The walls are metal plated and the room is so dark you can barely see the other end of it.")
        print("It's damp and too quiet as you hear the little splashing of puddles as you step through them.")
        print("The little clanging from the metal shards on the ground scrape against your shoes.")
        print("You see the floor getting illuminated by something.  With your weakness you look up and you notice")
        print("An illuminated barrier which has a box behind it.")
        print("This has got to be the bomb!")
        print("But it requires a code to remove the barrier!")
        print("\n")
        print("I can either go left or right to find this code. I'm sure it's in here. > ")
        action = input("left or right? > ")
        if action == "left":
            print("You decide to go left.")
            print("The clanging and splashing returns as you take a few steps across the room to the wall on the left")
            print("You are met with 3 buttons and what seems to be a riddle on the wall")
            print("I come once a minute, twice in a moment, but never in thousand years. What am l?")
            print("I see 3 buttons. The first one has T written under it, the second one M under it, and the 3rd has O")
            buttonanswer = input("One answer is correct - which do I choose? >" )
            if buttonanswer == "M":
                print("You choose the middle button. Your bony hands push against the sharp metal button.")
                print("You expect failure though you are met by the sound of what seems to be the barrier opening!")
                print("SUCCESS!")
                print("You run over to the barrier, wrench open the box and grab the bomb")
                return "the_bridge"

            else:
                print("You press the stone cold metal button. You hear the slicing of a pointy sharp object moving")
                print("as you see the shine of the spike which is followed by blood spraying over your head and")
                print("into your eyes!")

                return "death"
        else:
            print("You decide to go right and walk to the other end of the room.")
            print("Your strength fails you and you fall over on top of a pile of Gothon Claws.")
            print("With your dying breath you realise the claws have punctured your body and you bleed out.")

            return "death"

        print("")
        print("This scene is not yet configured. Subclass it and implement enter().")
        return "death"




class TheBridge():
    def enter(self):  # when you call function enter, it prints some stuff out
        print("This scene is not yet configured. Subclass it and implement enter().")
        print("you are now in the Bridge")
        return "death"

class EscapePod():
    def enter(self):  # when you call function enter, it prints some stuff out
        print("This scene is not yet configured. Subclass it and implement enter().")

class Map(object): #create an object called Map
    #define the dictionary of scenes - a look up table as such
    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge" : TheBridge(),
        "escape_pod" : EscapePod(),
        "death" : Death()
    }
    def __init__(self,start_scene):   #INSTANTIATING PUTS "CNETRAL_CORRIDOR AS START_SCENE VARIABLE"
        self.start_scene = start_scene
        print(self.start_scene)  #IT WILL PRINTOUT THE START-SCENE NAME

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene) #NEXT SCENE IS START-SCENE WHICH IS CENTRAL CORRIDOR.


#anyScene=Scene()  #create an instance of a Scene and call it anyScene
#anyScene.enter()

a_map = Map("central_corridor")  #CREATE AN INSTANCE OF MAP, INITIALISE WITH "CENTRAL CORRIDOR"
a_game = Engine(a_map) #CREATE AN INSTANCE OF ENGINE, INITIALISE WITH THE MAP INSTANCE YOU CREATED ABOVE
                        #THE MAP INSTANCE ONLY HAS 'CENTRAL CORRIDOR' AT THE MOMENT.
a_game.play() #NOW WE CALL THE PLAY METHOD IN THE ENGINE INSTANCE.


#what happens?
