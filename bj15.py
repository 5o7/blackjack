import turtle
import random

# Player has 7 characteristics: name, bank, bust, hand, hnd2, hnd3, hnd4, bet1, bet2

class Player:
	def __init__(self):
		name = None; bank = None; bust = None; hand = None
		hnd2 = None; hnd3 = None; hnd4 = None; bet1 = None; bet2 = None

p0 = Player(); p0.name = 'Dealer'; p0.bank = 999; p0.bust = False; 
p0.hand = []; p0.hnd2 = []; p0.hnd3 = []; p0.hnd4 = []; p0.bet1 = 0; p0.bet2 = 0
p1 = Player(); p1.name = 'Stevie'; p1.bank = 200; p1.bust = False; 
p1.hand = []; p1.hnd2 = []; p1.hnd3 = []; p1.hnd4 = []; p1.bet1 = 0; p1.bet2 = 0
p2 = Player(); p2.name = 'Freddy'; p2.bank = 200; p2.bust = False; 
p2.hand = []; p2.hnd2 = []; p2.hnd3 = []; p2.hnd4 = []; p2.bet1 = 0; p2.bet2 = 0
p3 = Player(); p3.name = 'Kristo'; p3.bank = 200; p3.bust = False; 
p3.hand = []; p3.hnd2 = []; p3.hnd3 = []; p3.hnd4 = []; p3.bet1 = 0; p3.bet2 = 0
p4 = Player(); p4.name = 'Carlie'; p4.bank = 200; p4.bust = False; 
p4.hand = []; p4.hnd2 = []; p4.hnd3 = []; p4.hnd4 = []; p4.bet1 = 0; p4.bet2 = 0

# Add dealer to the players list

players = [p0]

# The variable p holds the current player

p = players[0]

# Create a variable to allow/prevent actions

stage = 'adds'

# A tool to print info at intervals

counter = 0

# Create a deck of cards, call the list deck, and make 5 copies of the shuffled deck

d = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = []

for i in range(4 * 5):
	random.shuffle(d)
	for j in d:
		deck.append(j)

# Create the turtle window

wn = turtle.Screen()
wn.setup(480, 820)
wn.title('Blackjack')
wn.tracer(0)

# Create the turtle pens to write the interface

out = turtle.Turtle()
out.ht()
out.penup()
out.goto(-70, 30)
out.write('How many players? (1 - 4)', 
	align = 'left', font = ('Arial', 16, 'normal'))

pens = []

for i in range(0, len(players)):
	pen = turtle.Turtle()
	pen.ht()
	pen.penup()

	if i == 0:
		pen.goto(-50, 200)
		pen.write(players[i].name,
			align = 'left', font = ('Arial', 16, 'normal'))
	
	else:
		pen.goto(-340 + i * 120, -200)
		pen.write(players[i].name + ' | $' + str(players[i].bank) +
			'\nBet: $0',
			align = 'left', font = ('Arial', 16, 'normal'))
	pens.append(pen)

# This function is called when a card is dealt

def update_pens(a):

	# Clear the pens

	for i in pens:
		i.clear()

	# Write each player's info using this for loop

	for i in range(0, len(players)):

		# Make some variables to hold info. s = cards, b = bust, x = total

		s = b = ''
		x = 0

		# Total the player's count and put it in x

		for j in range(0, len(players[i].hand)):
			x = x + players[i].hand[j]

			# If player is over 21, update player as bust = true

			if players[i].bust == True:
				b = 'BUST'

		# Make a string of the player's cards

		for j in range(0, len(players[i].hand)):
			s = s + '\n' + str(players[i].hand[j])

		# Special pen placement for dealer

		if i == 0:
			pen.goto(-50, 200)

			# If it's the dealer's turn...

			if a.name == 'Dealer':

				# Write dealer's name, cards (s), total (x), and if busted (b)

				pen.write(players[i].name + 
					s + '\n---\n' + str(x) + '\n' + b,
					align = 'left', font = ('Arial', 16, 'normal'))

			# Write dealer's info but hide first card and score

			else:
				s = ''

				for j in range(0, len(players[i].hand)):
					if j == 0:
						s = s + '\n' + 'x'
					else:
						s = s + '\n' + str(players[i].hand[j])

				# Check to see if the dealer has cards or not

				if x > 0:
					pen.write(players[i].name + 
						s + '\n---\n' + '\n' + b,
					align = 'left', font = ('Arial', 16, 'normal'))

				else: 
					pen.write(players[i].name,
					align = 'left', font = ('Arial', 16, 'normal'))

		# Place player data in a row

		else:
			pen.goto(-330 + i * 115, -200)

			ins = ''

			if players[i].bet2 > 0:
				ins = '\nSecurity: ' + str(players[i].bet2)
				print(ins)

			# Write each player's name, bet amount, cards, total, and bust status

			if x > 0:
				pen.write(players[i].name + ' | $' + str(players[i].bank) + ins +
					'\nBet: ' + str(players[i].bet1)
					 + s + '\n---\n' + str(x) + '\n' + b,
					align = 'left', font = ('Arial', 16, 'normal'))

			# Do not write player count if there are no cards dealt.

			else:
				pen.write(players[i].name + ' | $' + str(players[i].bank) + 
					'\nBet: ' + str(players[i].bet1),
					align = 'left', font = ('Arial', 16, 'normal'))

# Handle asking each player if they want insurance

def handle_insurance(a):

	# Clear the pens

	for i in pens:
		i.clear()
	
	# Write each player's info using this for loop

	for i in range(0, len(players)):

		# Make some variables to hold info. s = cards, b = bust, x = total

		s = ''
		x = 0

		# Total the player's count and put it in x

		for j in range(0, len(players[i].hand)):
			x = x + players[i].hand[j]

		# Make a string of the player's cards

		for j in range(0, len(players[i].hand)):
			s = s + '\n' + str(players[i].hand[j])

		# Special pen placement for dealer

		if i == 0:
			pen.goto(-50, 200)

			# Write dealer's info but hide first card and score

			s = ''

			for j in range(0, len(players[i].hand)):
				if j == 0:
					s = s + '\n' + 'x'
				else:
					s = s + '\n' + str(players[i].hand[j])

			pen.write(players[i].name + s,
				align = 'left', font = ('Arial', 16, 'normal'))

		else:

			# Place player data in a row

			pen.goto(-330 + i * 115, -200)

			# Write each player's name, bet amount, cards, total, and bust status

			if players[i] == a:

				pen.write(players[i].name + ' | $' + str(players[i].bank) + 
					'\nBet: ' + str(players[i].bet1)
					+ s + '\n---\n' + str(x) + '\n' + '\nSecurity?\nY or N',
					align = 'left', font = ('Arial', 16, 'normal'))

			else:

				ins = ''
				if players[i].bet2 > 0:
					ins = '\nSecurity: ' + str(players[i].bet2)
					print(ins)

				pen.write(players[i].name + ' | $' + str(players[i].bank) + ins +
					'\nBet: ' + str(players[i].bet1)
					+ s + '\n---\n' + str(x),
					align = 'left', font = ('Arial', 16, 'normal'))

# Calculate the player's count

def get_count(a):
	x = 0
	for i in a.hand:
		x = x + i

	return (x)

# Calculate hand counts

def count_hands():
	_x1 = _x2 = _x3 = _x4 = 0
	for i in p1.hand:
		_x1 = _x1 + i
	for i in p2.hand:
		_x2 = _x2 + i
	for i in p3.hand:
		_x3 = _x3 + i
	for i in p4.hand:
		_x4 = _x4 + i
	_counts = [0, _x1, _x2, _x3, _x4]

	return(_counts)

# Call this after all the players have finished

def dealers_turn():
	global stage

	stage = 'start'

	while True:

		# Get the dealer's count

		x = get_count(p)

		# If dealer count less than 17, draw a card from the deck

		if x < 17:
			p.hand.append(deck[-1])
			deck.pop()

		# The dealer's count is over 17

		else:

			# Make a list called counts that holds player's counts

			counts = count_hands()
			
			# Make a list of strings 

			s = ['', '', '', '', '']

			# If dealer's count is less than 22...

			if x < 22:

				# For every player in the player's list,

				for i in range(1, len(players)):

					# Check if player busted

					if counts[i] > 21:
						s[i] = 'Dealer beats ' + players[i].name + '.'

					else:

						# If dealer is higher than player count, dealer wins

						if x > counts[i]:
							s[i] = 'Dealer beats ' + players[i].name + '.'

						# If player count is higher than dealers, player wins

						elif counts[i] > x:
							s[i] = players[i].name + ' beats Dealer.'
							players[i].bank = players[i].bank + players[i].bet1 * 2

						# Or else it's a tie

						else:
							s[i] = players[i].name + ' and Dealer push.'
							players[i].bank = players[i].bank + players[i].bet1

						print('----')
						print(len(players[i].hand))
						print(counts[i])
						print('----')

						# Handle natural blackjack

						if len(players[i].hand) == 2 and counts[i] == 21:
							print('player has a 21')
							s[i] = s[i] + ' Natural 21!'
							players[i].bank = players[i].bank + int(players[i].bet1 * 0.5)

					# Settle security

					if x > 17 and len(p.hand) >= 2:
						if players[i].bet2 > 0:
							players[i].bank = players[i].bank + players[i].bet2
							s[i] = s[i] + ' Security: ' + str(players[i].bet2) + ' settled.'

			# Dealer is over 21 and busts

			else:
				p.bust = True

				for i in range(1, len(players)):
					if players[i].bust == False:
						s[i] = players[i].name + ' beats Dealer.'

						# Handle natural blackjack

						if len(players[i].hand) == 2 and counts[i] == 21:
							print('player has a 21')
							s[i] = s[i] + ' Natural 21!'
							players[i].bank = players[i].bank + int(players[i].bet1 * 0.5)

						players[i].bank = players[i].bank + players[i].bet1 * 2
					else:
						s[i] = players[i].name + ' busts.'
			
			
			# Convert the s list, into one string

			out_text = ''
			for i in s:
				out_text = out_text + '\n' + i

			out_text = out_text + '\n\n(S)tart Game'

			# Print results

			out.clear()
			out.write(out_text, align = 'left', font = ('Arial', 16, 'normal'))

			update_pens(p)

			# Get out of the dealer's turn

			break

# Cycle through player turns

def change_players():
	global p

	i = players.index(p)

	if i == len(players) - 1:
		p = players[0]
		dealers_turn()

	else:
		p = players[i + 1]


	
# Write the betting amounts

def start_place_bets():
	global stage
	global players
	global p

	p = players[1]
	update_pens(p)
	stage = 'bets'
	out.clear()
	out.write('Place bets:\n---------------\n' + 
		'(1)  $10\n(2)  $20\n(3)  $30\n(4)  $40', 
		align = 'left', font = ('Arial', 16, 'normal'))

# Place bets

def next_bet():
	global p
	global stage

	i = players.index(p)

	if i == len(players) - 1:
		p = players[1]
		out.clear()
		out.write('(D)eal', align = 'left', font = ('Arial', 16, 'normal'))
		stage = 'deal'
	else:
		p = players[i + 1]

# Reset game

def press_d():
	global p
	global stage

	if stage == 'deal':

		# Set everyone's bust to false, empty all hands, place all bets

		for i in players:
			i.bust = False
			i.hand = []
			i.bet2 = 0
			i.bank = i.bank - i.bet1

		# Empty the Dealer's hand

		p0.hand = []

		# Deal two cards to all players

		for i in range(0, 2):
			for i in players:
				i.hand.append(deck[-1])
				deck.pop()

		# Use a variable, p, to hold the current player

		p = players[1]

		if players[0].hand[1] == 11:

			out.clear()
			out.write('Dealer has an ace.', 
				align = 'left', font = ('Arial', 16, 'normal'))

			handle_insurance(p)

			stage = 'insurance'

		# Clear previous outcome and update pens

		else:

			if 8 < p.hand[0] + p.hand[1] < 12:
				stage = 'double'
				out.clear()
				out.write('Total 9, 10, or 11\nDouble Down?\n(Y)es or (N)o', 
					align = 'left', font = ('Arial', 16, 'normal'))

			else:
				stage = 'hit or pass'
				out.clear()
				out.write('(H)it or (P)ass', 
					align = 'left', font = ('Arial', 16, 'normal'))

			update_pens(p)
	
# Function to add a card to the current player

def press_h():
	global p
	global stage

	if stage == 'hit or pass':

		# Current player draws a card from the deck

		p.hand.append(deck[-1])
		deck.pop()

		# Get the player's count

		x = get_count(p)

		# Check all the player's cards for an ace

		for i in range(len(p.hand)):

			# If player busts with an ace, set the ace equal to one

			if p.hand[i] == 11 and x > 21:
				p.hand[i] = 1
				break

		# Get player count again.

		x = get_count(p)

		# If player's count is over 21, change player

		if x > 21:

			p.bust = True

			change_players()
					

		# Display everyone's hand

		update_pens(p)

# Change to the next player

def press_p():
	global p
	global stage

	if stage == 'hit or pass':
		change_players()

		if p != players[0]:
			if 8 < p.hand[0] + p.hand[1] < 12:
				print('Double down?')
				stage = 'double'
				out.clear()
				out.write('Total 9, 10, or 11\nDouble Down?\n(Y)es or (N)o', 
					align = 'left', font = ('Arial', 16, 'normal'))

# User input for bet amounts

def press_1():
	global stage
	global players
	global p

	if stage == 'bets':
		p.bet1 = 10

		next_bet()
		update_pens(p)

	if stage == 'adds':
		players = [p0, p1]
		p = players[1]
		start_place_bets()

def press_2():
	global stage
	global players
	global p

	if stage == 'bets':
		p.bet1 = 20

		next_bet()
		update_pens(p)

	if stage == 'adds':
		players = [p0, p1, p2]
		start_place_bets()

def press_3():
	global stage
	global players
	global p

	if stage == 'bets':
		p.bet1 = 30

		next_bet()
		update_pens(p)

	if stage == 'adds':
		players = [p0, p1, p2, p3]
		start_place_bets()

def press_4():
	global stage
	global players
	global p

	if stage == 'bets':
		p.bet1 = 40

		next_bet()
		update_pens(p)

	if stage == 'adds':
		players = [p0, p1, p2, p3, p4]
		start_place_bets()

def press_y():
	global p
	global stage

	if stage == 'insurance':

		p.bet2 = int(p.bet1 * 0.5)

		p.bank = p.bank - p.bet2

		i = players.index(p)

		if i == len(players) - 1:
			p = players[1]
			out.clear()
			out.write('(H)it or (P)ass', align = 'left', font = ('Arial', 16, 'normal'))
			stage = 'hit or pass'
			update_pens(p)

		else:
			p = players[i + 1]
			handle_insurance(p)

	if stage == 'double':

		p.bank = p.bank - p.bet1
		p.bet1 = p.bet1 * 2
		out.clear()
		out.write('(H)it or (P)ass', align = 'left', font = ('Arial', 16, 'normal'))
		update_pens(p)
		stage = 'hit or pass'

def press_n():
	global p
	global stage
	
	if stage == 'insurance':
		
		i = players.index(p)

		if i == len(players) - 1:
			p = players[1]
			out.clear()
			out.write('(H)it or (P)ass', align = 'left', font = ('Arial', 16, 'normal'))
			stage = 'hit or pass'
			update_pens(p)

		else:
			p = players[i + 1]
			handle_insurance(p)

	if stage == 'double':
		out.clear()
		out.write('(H)it or (P)ass', align = 'left', font = ('Arial', 16, 'normal'))
		update_pens(p)
		stage = 'hit or pass'

def press_s():
	global p
	global stage

	if stage == 'start':
		out.clear()
		out.write('Place bets:\n---------------\n' + 
			'(1)  $10\n(2)  $20\n(3)  $30\n(4)  $40', 
			align = 'left', font = ('Arial', 16, 'normal'))

		# Set everyone's bust to false, empty all hands

		for i in players:
			i.bust = False
			i.hand = []
			i.bet1 = 0
			i.bet2 = 0
			i.bank = i.bank - i.bet1

		p = players[1]

		update_pens(p)

		stage = 'bets'

turtle.listen()
turtle.onkey(press_d, 'd')
turtle.onkey(press_h, 'h')
turtle.onkey(press_p, 'p')
turtle.onkey(press_1, '1')
turtle.onkey(press_2, '2')
turtle.onkey(press_3, '3')
turtle.onkey(press_4, '4')
turtle.onkey(press_y, 'y')
turtle.onkey(press_n, 'n')
turtle.onkey(press_s, 's')

while True:
	wn.update()

	counter = counter + 1
	if counter % 20000 == 0:
		print(p.name)
		print(stage)
