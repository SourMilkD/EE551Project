import time

def intro():
#Intro to Adventure
    player_name = input("What's your name? > ")
    player_name.capitalize()
    print("{}, you are trapped in your own dream.".format(player_name.capitalize()))
    time.sleep(2)
    print("This is a dungeon with multiple exits, meaning your escape is dependent on your decisions.")
    time.sleep(3)
    print("Think logically and carefully or your mistakes will lead to your never-ending sleep.")
    time.sleep(3)
    print("I am your subconcious voice that will help guide you, choose one of the marked passages.")
    time.sleep(3)
    print("-- you realize you're in the middle of room with 4 sides, a corridor leads off on each side --")
    time.sleep(3)
    start_passage()

def start_passage():
#4 different story lines diverge from your first decision
    
    start_path = input("1, 2, 3, or 4? > ")

    if start_path == "1":
        print("-- you walk down the passage from the side marked {} --".format(start_path))
        time.sleep(2)
        print("-- you enter a room to see a dog tied to a stake in the ground and another passage --")
        time.sleep(2)
        passage1()
    elif start_path == "2":
        print("-- you walk down the passage from the side marked {} --".format(start_path))
        time.sleep(2)
        print("-- you enter a room to see a cat tied to a stake in the ground and another passage --")
        time.sleep(2)
        passage2()
    elif start_path == "3":
        print("-- you walk down the passage from the side marked {} --".format(start_path))
        time.sleep(2)
        print("-- you enter a room to see a wolf chained to a stake in the ground and another passage --")
        time.sleep(2)
        passage3()
    elif start_path == "4":
        print("-- you walk down the passage from the side marked {} --".format(start_path))
        time.sleep(2)
        print("-- you enter a room find a horse tied to a stake in the ground and another passage --")
        time.sleep(2)
        passage4()
    else:
        print("Decide either 1, 2, 3, or 4 for your decision or we'll be here forever...")
        time.sleep(2)
        start_passage()

### 1 2 3 4 Passages ###

def passage1():
    choice1 = input("Do you free the dog? > ")
    pet = "dog"

    if choice1 == "yes":
        print("The dog decides to accompany you! The dog is as fast as you and small, not very strong but very loving.")
        time.sleep(2)
        print("-- you make your way down the passage with the dog as the previous passage entrance closes --")
        time.sleep(2)
        print("-- you are at a fork in the passage with two passages leading off infront of you --")
        time.sleep(2)
        passageLR()
    
    elif choice1 == "no":
        print("-- you pass the dog and as you enter the next passage you hear a wimper and look back --")
        time.sleep(2)
        print("-- the dog is gone and the passage you came from is closed off, you can only continue this passage --")
        solo_route()

    else:
        print("Provide a clear choice or we'll be here forever...")
        time.sleep(2)
        passage1()

def passage2():
    choice1 = input("Do you free the cat? > ")
    pet = "cat"
    
    if choice1 == "yes":
        print("The cat decides to accompany you! The cat is as nimble as you and small, not very strong and very selfish.")
        time.sleep(2)
        print("-- you make your way down the passage with the cat as the previous passage entrance closes --")
        time.sleep(2)
        print("-- you are at a fork in the passage with two passages leading off infront of you --")
        time.sleep(2)
        passageLR()
    
    elif choice1 == "no":
        print("-- you pass the cat and as you enter the next passage you hear a purr and look back --")
        time.sleep(2)
        print("-- the cat is gone and the passage you came from is closed off, you can only continue this passage --")
        solo_route()

    else:
        print("Provide a clear choice or we'll be here forever...")
        time.sleep(2)
        passage2()

def passage3():
    choice1 = input("Do you free the wolf? > ")
    pet = "wolf"
    
    if choice1 == "yes":
        print("The wolf decides to accompany you! The wolf is very swift and quite large, it is a strong pet and very loyal.")
        time.sleep(2)
        print("-- you make your way down the passage with the wolf as the previous passage entrance closes --")
        time.sleep(2)
        print("-- you are at a fork in the passage with two passages leading off infront of you --")
        time.sleep(2)
        passageLR()
    
    elif choice1 == "no":
        print("-- you pass the wolf and as you enter the next passage you hear a growl and look back --")
        time.sleep(2)
        print("-- the wolf is gone and the passage you came from is closed off, you can only continue this passage --")
        solo_route()

    else:
        print("Provide a clear choice or we'll be here forever...")
        time.sleep(2)
        passage3()

def passage4():
    choice1 = input("Do you free the horse? > ")
    pet = "horse"
    
    if choice1 == "yes":
        print("The horse decides to accompany you! The horse is fastest animal here and is quite large, it would never fight but is very loyal to you.")
        time.sleep(2)
        print("-- you make your way down the passage with the horse as the previous passage entrance closes --")
        time.sleep(2)
        print("-- you are at a fork in the passage with two passages leading off infront of you --")
        time.sleep(2)
        passageLR()
    
    elif choice1 == "no":
        print("-- you pass the horse and as you enter the next passage you hear a neigh and look back --")
        time.sleep(2)
        print("-- the horse is gone and the passage you came from is closed off, you can only continue this passage --")
        solo_route()

    else:
        print("Provide a clear choice or we'll be here forever...")
        time.sleep(2)
        passage2()

### Left, Right, Solo Passages ###

def passageLR():
    LorR = input(" Left or Right? > ")    
    if LorR == "left" or "Left" or "l" or "L":
        print("-- you start down the left path --")
        time.sleep(2)
        pet_name = input("Oh wait you haven't named your pet? Enter a name for your pet: ")
        print("You wake up and see {}, you had taken a quick nap from chopping wood in the log cabin you had built in the mountains years ago".format(pet_name))
        time.sleep(2)
        print("T")
        time.sleep(0.3)
        print("H")
        time.sleep(0.3)
        print("E")
        time.sleep(0.3)
        print(" ")
        time.sleep(0.3)
        print("E")
        time.sleep(0.3)
        print("N")
        time.sleep(0.3)
        print("D")

    elif LorR == "right" or "Right" or "r" or "R":
        print("-- you start down the right path --")
        time.sleep(2)
        pet_name = input("Oh wait you haven't named your pet? Enter a name for your pet: ")
        print("You wake up and see {}, you had taken a quick nap from doing work in the rice paddies in your life of solitude in a country of poverty.".format(pet_name))
        time.sleep(2)
        print("T")
        time.sleep(0.3)
        print("H")
        time.sleep(0.3)
        print("E")
        time.sleep(0.3)
        print(" ")
        time.sleep(0.3)
        print("E")
        time.sleep(0.3)
        print("N")
        time.sleep(0.3)
        print("D")
    
    else:
        print("Provide a clear choice or we'll be here forever...")
        time.sleep(2)
        passageLR()

def solo_route():
    print("You decided to live a lonely life...")
    time.sleep(2)
    print("-- you wake up in a jail cell --")
    time.sleep(2)
    print("-- you realize you lived a life of crime from greed and jealousy and continue the life in a jail cell till you rot, all by yourself --")
    time.sleep(2)
    print("T")
    time.sleep(0.3)
    print("H")
    time.sleep(0.3)
    print("E")
    time.sleep(0.3)
    print(" ")
    time.sleep(0.3)
    print("E")
    time.sleep(0.3)
    print("N")
    time.sleep(0.3)
    print("D")
##### END OF STORY #####

if __name__ == '__main__':
    intro()