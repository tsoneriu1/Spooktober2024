import random, math
from utils import print_house,print_title,print_ghost

haunted_room = 4 #default
haunted_room2 = 16 #default


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
    global haunted_room2


    rooms = 5
    if difficulty == "6":
        rooms = 20

    print("There are " + str(rooms) + " rooms.")
    haunted_room = random.randint(1,rooms+1) 
    if difficulty == "6":
        haunted_room2 = random.randint(1,rooms)
        if haunted_room == haunted_room2:
            haunted_room2 += 1
    if difficulty == "6":
        print("The twins are in separated in different rooms, help bring them together")
    else:
        print("The ghost is haunting one of the rooms in the house, find the ghost")
    print_ghost(difficulty)
    haunted = True
    if difficulty == "6":
        haunted2 = True
    else:
        haunted2 = False
    investigate_counter = 0
    
    if difficulty =="6":
        haunted_rooms = []
        haunted_rooms.append(haunted_room)
        haunted_rooms.append(haunted_room2)



        while haunted_rooms:
            room_range = range(1,rooms+1)
            room_choice = ", ".join(str(num) for num in room_range)
            response = input("Choose a room to investigate: " + room_choice + "\n")
            response = int(response)
            if response in room_range:
                print("Investigating room ", response)
                if response in haunted_rooms:
                    haunted_rooms.remove(response)
                    if not haunted_rooms:
                        print("You found both of the twins")
                        print_ghost(difficulty)
                        print("Thanks for playing, you saved the day!")    
                        exit()
                    print("You found one of the twins")

                else:
                    print("No ghosts here")
                    #no movement, game takes too long

        
    else:
        while haunted:
            room_range = range(1,rooms+1)
            room_choice = ", ".join(str(num) for num in room_range)
            response = input("Choose a room to investigate: " + room_choice + "\n")
            response = int(response)
            if response in room_range:
                check = haunted_room

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
# 6 20 rooms (worst case 20 tries), ghosts won't move in this to make it faster.

print_title()

difficulty = input("Choose difficulty: \n" +
                   "1: Classic (normal)\n"+
                   "2: Poltergeist (easy)\n"
                   "3: Brownie (hard)\n"+
                   "4: Sprite (normal, time limit)\n"+
                   "5: Wraith (hard, time limit)\n"
                   "6: Haunted Hotel Twins, (normal, more rooms, more ghosts)")

if difficulty in ['1','2','3','4','5','6']:
    ghosthunter(difficulty)
else:
    ghosthunter(1)
