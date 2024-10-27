# Spooktober2024



## Ghosthunter Game 👻

You are a ghosthunter and need to search a haunted house for a ghost. 
There are 5 rooms in the house that could be haunted. 
The ghost can move during the night to an adjecent room. 
You can search during the day when it is safe, and it takes all day to setup and take down all of your paranormal sensing equipment, so you can only search one room at a time.
The goal is to find the ghost as quickly as possible.

### Game Modes

* Classic. Regular gameplay.
* Poltergeist. This ghost is loud and can give the play hints to where it is located. This can make the game easier.
* Brownie. This entity has random movement. This is harder since the movement is not predictable. Player cannot use the normal strategy of expecting the ghost to show up in odd or even spaces, or select the same location expecting the ghost to move into it.
* Sprite. The game is over when the entity disapears in 6 turns. This is the worst case for finding the ghost in 5 rooms.
* Wraith: The game is over in 3 turns, and the ghost moves randomly. This is much harder and the player needs to be lucky to win.
* Haunted Hotel Twins: This game has increased the number of rooms to 20, and one additional ghost. There is no ghost movement in this mode to keep game time low.


#### Inspiration
This game is based on the logic puzzle "Fox in the hole", also inspired by the game "Phasmophobia", a co-op horror game where you and your friends use ghost-hunting equipment to gather evidence of paranormal activity and figure out what type of paranormal entity is haunting the area. 
The puzzle has a fox and 5 holes. Each night the fox moves to an adjecent hole. During the day you can search one hole. The goal is to find the fox. The worst case is 2(n-2) for the number of holes. For this game the ghost replaces the fox and instead of holes its a haunted house with different rooms. There are also different behaviours for the ghost that makes the game more interesting.

### How To Play

Run the ghosthunter.py file

```
python ghosthunter.py
```

Select the room number to search until you can find the ghost.