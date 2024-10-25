import random, math
from utils import print_house,print_title,print_ghost

haunted_room = 3 #default


def move_ghost(difficulty):

    global haunted_room

    new_room =  haunted_room
    if new_room == 1:
        new_room += 1
    elif new_room == 5:
        new_room -= 1
    else:
        chance = random.random()*100
        if chance < 50:
            new_room += 1
        else:
            new_room -= 1

    haunted_room = new_room

    if difficulty == "3" or difficulty == "5": # elusive or aggressive ghost, random movement
        haunted_room = random.randint(1,5) 
    
    print("The ghost has moved.")
    if difficulty == "2": # obvious ghost, clues to location
        if haunted_room == 1 or haunted_room == 5:
            print("You see the ghost by the windows, check the ends of the house.")
        if haunted_room == 3:
            print("There are strange footprints in the hallways, check the middle of the house.")
        if haunted_room == 2:
            print("Strange noises coming from the left.")
        if haunted_room == 4:
            print("The lights went out on the right side of the house.")


def ghosthunter(difficulty):
    print("The Ghosthunter")


    print_house()
    
    global haunted_room

    haunted_room = random.randint(1,5) 
    print("The ghost is haunting one of the rooms in the house, find the ghost")
    print_ghost(difficulty)
    haunted = True
    investigate_counter = 0
    
    while haunted:
        print(investigate_counter)
        response = input("Choose a room to investigate: 1,2,3,4,5\n")

        if response in ['1','2','3','4','5']:
            check = str(haunted_room)

            print("Investigating room ", response)
            if check == response:
                haunted = False
                print("You found the ghost")
                print_ghost(difficulty)
                print("Thanks for playing, you saved the day!")
                exit()
            else:
                print("Ghost isn't here")
                if difficulty == "4":
                    investigate_counter += 1
                    if investigate_counter > 5:
                        print("The ghost got away")
                        print_ghost(difficulty)
                        print("Game Over")
                        exit()
                    if investigate_counter > 1:
                        print("Hurry! The ghost won't stick around")
                if difficulty == "5":
                    investigate_counter += 1
                    if investigate_counter == 1:
                        print("The ghost knows your there...")
                    if investigate_counter == 2:
                        print("You have a bad feeling about this...")
                    if investigate_counter > 3:
                        print("The ghost has found you!")
                        print_ghost(difficulty)
                        print("Game Over")
                        exit()

                move_ghost(difficulty)

# difficulty
# 1 Classic
# 2 Ghost gives clues
# 3 Random ghost movement
# 4 ghost escapes in 6 days or tries, worst case is 2(n-2), or 6 for 5 rooms
# 5 ghost catches you in 3 days, random movement

print_title()

difficulty = input("Choose difficulty: \n" +
                   "1: Classic\n"+
                   "2: Obvious Ghost\n"
                   "3: Sneaky Ghost\n"+
                   "4: Elusive Ghost\n"+
                   "5: Agressive Ghost\n")

if difficulty in ['1','2','3','4','5']:
    ghosthunter(difficulty)
else:
    ghosthunter(1)
