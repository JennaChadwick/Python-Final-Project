# Python-Final-Project
Python Programming - FALL 2020 CS 3080 SEC001 Jenna Chadwick and Andrew Nguyen


## General Description
  Users will interact with a Discord Bot to play a scavenger hunting game. The scavenger hunting game includes text files containing randomly hidden items: Junk or Treasure.
  For users to play the scavenger hunting game with the bot, the user would need to be assigned a role,'admin', in Discord by right-clicking on the channel profile and click server settings-role.
  Users assigned to that role can play the game with the bot. To interact with the bot, users can input pre-defined Discord commands. 
  Once users input a command, the bot will respond with a message aboout what hidden item they found.
  

## Text Files Description
  * junk.txt: A list of random items of no use. These are just flavor and have no bearing on the game
  * treasure.txt: A list of useful items, which can be used by the player in other games.
  * jackpot.txt: If a result of "Afamiliar" is read from the treasure file, a result from this file is given to the player instead. these are particularly rare, unique, or valuable rewards.
  * pets.txt: A list of all registered pet ids and their associated luck values
  * userinfo.txt: A list of player ids, the time they last called a timed function, and their owned pets
  * usertime.txt is obsolete and can be deleted



## Discord commands(starts with a dot)
* .userRead: to read the Discord username from userInfo Text file
* .userName: to print one's username
* .time:  to print the current time
* .scavenge: takess one argument, in the format #xxxx. It then uses that as a pet ID, checks to make sure you own the pet, and determines the luck of the pet. It then rolls to see if you get a junk
  or treasure item.
* .editPet: To edit pets. Luck and Owner are optional arguments
* .start: To add an owner






