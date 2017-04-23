from random import *
qplayer = 0
decks = 0
roll_1 = 0
player_var = 1
all_decks = ['Tricksters','Ninjas','Dinosaurs','Aliens','Pirates','Wizards','Robots','Zombies']
OC_deck = ['Minions of Cthulhu','Elder Things','Innsmouth','Miskatonic University']
AL_deck = ['Cyborg Apes','Shapeshifters','Super Spies','Time Travelers']
SF_deck = ['Bear Cavalry','Ghosts','Killer Plants','Steampunks']
print "Welcome to the Smash Up Randomizer!, It's a fair way to choose a completely random deck at random for every player!\n"
print "How many players will you have?"
qplayer = int(raw_input())
for rolls in range(qplayer):
	print "Player Roll to choose a deck first y/n?" 
	ver_yes = raw_input()
	if ver_yes == 'y':
		roll = randint(1,6)
		print "you've rolled " + str(roll)
print "Which Expansions would you like to include?\n"
print "Please type a list of two capitalized letters for each set you have, with spaces in between each designation\n"
print "For Obligatory Cthulhu, type OC\n"
print "For Awesome Level 9000, type AL\n"
print "Science Fiction Double Feature type SF\n"
print "For Example: AL SF OC <-- yields a list of the base decks and 3 expansions\n"
deck_select = raw_input()
deck_select_string = deck_select.split()
for d in deck_select_string:
	if d == 'OC':
		all_decks.extend(OC_deck)
	if d == 'AL':
		all_decks.extend(AL_deck)
	if d == 'SF':
		all_decks.extend(SF_deck)
print "You've selected the following decks:" + str(all_decks) + '\n'
for z in range(qplayer):
	print "Player " + str(player_var)+" Roll for your first deck y/n?" 
	ver_yes1 = raw_input()
	print "available decks are " + str(all_decks)
	if ver_yes1 == 'y':
		roll = choice(all_decks)
		print "you've rolled " + str(roll)
		player_var += 1
		all_decks.remove(roll)
player_var = 1
for r in range(qplayer):
	print "Player " + str(player_var)+" Roll for your second deck y/n?"
	ver_yes2 = raw_input()
	print "available decks are " + str(all_decks)
	if ver_yes2 == 'y':
		roll = choice(all_decks)
		print "you've rolled " + str(roll)
		player_var += 1
		all_decks.remove(roll)
player_var = 1
for v in range(qplayer):
	print "Player " + str(player_var)+" Roll to take the first turn y/n?"
	first_turn = raw_input()
	if first_turn == 'y':
		roll = randint(1,6)
		print "you've rolled " + str(roll)
		player_var += 1
print "Godspeed, may the strange creatures you've selected bring you victory!..."
exit()

