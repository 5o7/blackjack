import turtle
import random

# Player has five characteristics.

class Player:
	def __init__(self):
		name = None
		bet = None
		bank = None
		bust = None
		hand = None

p0 = Player(); p0.name = 'Dealer'; p0.bet = 0; p0.bank = 999; p0.bust = False; p0.hand = []
p1 = Player(); p1.name = 'Stevie'; p1.bet = 0; p1.bank = 200; p1.bust = False; p1.hand = []
p2 = Player(); p2.name = 'Freddy'; p2.bet = 0; p2.bank = 200; p2.bust = False; p2.hand = []
p3 = Player(); p3.name = 'Kristo'; p3.bet = 0; p3.bank = 200; p3.bust = False; p3.hand = []
p4 = Player(); p4.name = 'Carlie'; p4.bet = 0; p4.bank = 200; p4.bust = False; p4.hand = []

# Add players to the players list, including the dealer.

players = [p0, p1, p2, p3, p4]

# p will be the player who is up. p1 will be up first.

p = players[1]

# The counts list is used to hold all of the player's hand counts.

counts = []

counter = 0

# Create a variable to allow/prevent actions

stage = 'bets'

# Create a deck of cards. Call the list deck. Make 5 copies of the shuffled deck.

d = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
deck = []

for i in range(5):
	random.shuffle(d)
	for j in d:
		deck.append(j)

# Create the turtle window

wn = turtle.Screen()
wn.setup(480, 820)
wn.tracer(0)
pens = []

# Create the turtle pens that write the scores.

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

out = turtle.Turtle()
out.ht()
out.penup()
out.goto(-70, 30)
out.write('Place bets:\n---------------\n' + 
	'(1)  $10\n(2)  $20\n(3)  $30\n(4)  $40\n(5)  $50', 
	align = 'left', font = ('Arial', 16, 'normal'))

# This function is called when a card is dealt.

def update_pens(a):

	# Clear the pens.

	for i in pens:
		i.clear()

	# Write each player's info using this for loop.

	for i in range(0, len(players)):

		# Make some variables to hold info. s = cards, b = bust, x = total

		s = b = ''
		x = 0

		# Total the player's count and put it in x.

		for j in range(0, len(players[i].hand)):
			x = x + players[i].hand[j]

			# If player is over 21, update player as bust = true.

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

				# Write dealer's name, cards (s), total (x), and if busted (b).

				pen.write(players[i].name + 
					s + '\n---\n' + str(x) + '\n' + b,
				align = 'left', font = ('Arial', 16, 'normal'))

			else:

				# Write dealer's info but hide first card and score.

				s = ''
				for j in range(0, len(players[i].hand)):
					if j == 0:
						s = s + '\n' + 'x'
					else:
						s = s + '\n' + str(players[i].hand[j])

				pen.write(players[i].name + 
					s + '\n---\n' + '\n' + b,
				align = 'left', font = ('Arial', 16, 'normal'))

		else:

			# Place player data in a row.

			pen.goto(-330 + i * 115, -200)

			# Write each player's name, bet amount, cards, total, and bust status.

			if x > 0:
				pen.write(players[i].name + ' | $' + str(players[i].bank) + 
					'\nBet: ' + str(players[i].bet)
					 + s + '\n---\n' + str(x) + '\n' + b,
					align = 'left', font = ('Arial', 16, 'normal'))

			# Do not write player count if there are no cards dealt.

			else:
				pen.write(players[i].name + ' | $' + str(players[i].bank) + 
					'\nBet: ' + str(players[i].bet),
					align = 'left', font = ('Arial', 16, 'normal'))

# Calculate the player's count.

def get_count(a):
	x = 0
	for i in a.hand:
		x = x + i

	return (x)

# This function is called to calculate all hand counts.

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

# This function is called after all the players have finished.

def dealers_turn():

	while True:

		# Get the dealer's count.

		x = get_count(p)

		# If dealer count less than 17, draw a card from the deck.

		if x < 17:
			p.hand.append(deck[-1])
			deck.pop()

		# The dealer's count is over 17.

		else:

			# Make a list called counts that holds player's counts.

			counts = count_hands()
			
			# Make some string variables

			s = ['', '', '', '', '']

			# If dealer's count is less than 22...

			if x < 22:

				# For every player in the player's list,

				for i in range(1, len(players)):

					# Check if player busted.

					if counts[i] > 21:
						s[i] = 'Dealer beats ' + players[i].name + '.'

					else:

						# If dealer is higher than player count, dealer wins.

						if x > counts[i]:
							s[i] = 'Dealer beats ' + players[i].name + '.'

						# If player count is higher than dealers, player wins.

						elif counts[i] > x:
							s[i] = players[i].name + ' beats Dealer.'
							players[i].bank = players[i].bank + players[i].bet * 2

						# Or else it's a tie.

						else:
							s[i] = players[i].name + ' and Dealer push.'
							players[i].bank = players[i].bank + players[i].bet

			# Dealer is over 21 and busts.

			else:
				p.bust = True

				for i in range(1, len(players)):
					if players[i].bust == False:
						s[i] = players[i].name + ' beats Dealer.'
						players[i].bank = players[i].bank + players[i].bet * 2
					else:
						s[i] = players[i].name + ' busts.'
			
			# Print results.

			out_text = ''
			for i in s:
				out_text = out_text + '\n' + i

			out.clear()
			out.write(out_text, align = 'left', font = ('Arial', 16, 'normal'))

			update_pens(p)

			# Get out of the dealer's turn.

			break

# This function is a bad way to change players.

def change_players():
	global p

	if p == players[1]:
		p = players[2]
	elif p == players[2]:
		p = players[3]
	elif p == players[3]:
		p = players[4]
	else:
		p = players[0]

		dealers_turn()


# Reset game.

def deal_me():
	global p
	global stage

	if stage == 'deal':

		# Set everyone's bust to false, empty all hands, place all bets.

		for i in players:
			i.bust = False
			i.hand = []
			i.bank = i.bank - i.bet

		# Empty the Dealer's hand.

		p0.hand = []

		# Deal two cards to all players.

		for i in range(0, 2):
			for i in players:
				i.hand.append(deck[-1])
				deck.pop()

		# Use a variable, p, to hold the current player.

		p = players[1]

		# Display everyone's hand and clear previous outcome.
		out.clear()
		out.write('(H)it or (P)ass', 
	align = 'left', font = ('Arial', 16, 'normal'))
		update_pens(p)
		stage = 'hit or pass'
	
# Function to add a card to the current player.

def hit_me():
	global p
	global stage

	if stage == 'hit or pass':
		# Current player draws a card from the deck.

		p.hand.append(deck[-1])
		deck.pop()

		# Get the player's count.

		x = get_count(p)

		# Check all the player's cards for an ace.

		for i in range(len(p.hand)):

			# If player busts with an ace, set the ace equal to one.

			if p.hand[i] == 11 and x > 21:
				p.hand[i] = 1
				break

		# Get player count again.

		x = get_count(p)

		# If player's count is over 21, change player

		if x > 21:

			p.bust = True

			change_players()
					

		# Display everyone's hand.

		update_pens(p)

# This function just changes to the next player.

def pass_me():
	global p
	global stage

	change_players()

	if p.name == 'Dealer':

		# The hand is complete. Update game stage

		stage = 'deal'

# Place bets

def next_bet():
	global p
	global stage

	if p == players[1]:
		p = players[2]
	elif p == players[2]:
		p = players[3]
	elif p == players[3]:
		p = players[4]
	else:
		p = players[1]
		out.clear()
		out.write('(D)eal', align = 'left', font = ('Arial', 16, 'normal'))
		stage = 'deal'

def bet_10():
	global p
	global stage

	if stage == 'bets':
		p.bet = 10

	next_bet()
	update_pens(p)


def bet_20():
	global p
	global stage

	if stage == 'bets':
		p.bet = 20

	next_bet()
	update_pens(p)

def bet_30():
	global p
	global stage

	if stage == 'bets':
		p.bet = 30

	next_bet()
	update_pens(p)

def bet_40():
	global p
	global stage

	if stage == 'bets':
		p.bet = 40

	next_bet()
	update_pens(p)

def bet_50():
	global p
	global stage

	if stage == 'bets':
		p.bet = 50

	next_bet()
	update_pens(p)

# Listen for keyboard input.

turtle.listen()
turtle.onkey(deal_me, 'd')
turtle.onkey(hit_me, 'h')
turtle.onkey(pass_me, 'p')
turtle.onkey(bet_10, '1')
turtle.onkey(bet_20, '2')
turtle.onkey(bet_30, '3')
turtle.onkey(bet_40, '4')
turtle.onkey(bet_50, '5')

# A loop to keep the game running.

while True:
	wn.update()






























