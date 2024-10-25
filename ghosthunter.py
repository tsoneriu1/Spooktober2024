import random, math

haunted_room = 3

def move_ghost():

    global haunted_room

    print(haunted_room)
    new_room =  haunted_room
    if new_room == 1:
        new_room += 1
    elif new_room == 5:
        new_room -= 1
    else:
        chance = random.random()*100
        print(chance)
        if chance < 50:
            new_room += 1
        else:
            new_room -= 1
    haunted_room = new_room
    print(haunted_room)

    print("The ghost has moved")





def ghosthunter():
    print("The Ghosthunter")
    
    # haunted_room = random.randint(1,5) 
    global haunted_room

    haunted_room = 3
    print("The ghost is haunting one of the rooms in the house, find the ghost")

    haunted = True
    
    while haunted:
        response = input("Choose a room to investigate: 1,2,3,4,5\n")

        print("haunted room " ,type(haunted_room), haunted_room)
        print("response " ,type(response), response)

        if response in ['1','2','3','4','5']:
            check = str(haunted_room)
            print("haunted room " ,type(haunted_room), haunted_room)
            print("check " ,type(check), check)

            print("Investigating room ", response)
            if check == response:
                haunted = False
                print("You found the ghost")
            else:
                print("Ghost isn't here")
                move_ghost()


ghosthunter()