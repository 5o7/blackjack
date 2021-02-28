import turtle
import random

# Player has 7 attributes: name, bank, bust, hand, bet1, bet2

class Player:
	def __init__(self):
		name = None; bank = None; bust = None; hand = None; bet1 = None; bet2 = None; boss = None

p0 = Player(); p0.name = 'Dealer'; p0.bank = 999; p0.bust = False; p0.hand = []; p0.bet1 = 0; p0.bet2 = 0; p0.boss = 0
p1 = Player(); p1.name = 'Stevie'; p1.bank = 100; p1.bust = False; p1.hand = []; p1.bet1 = 0; p1.bet2 = 0; p1.boss = 1
p2 = Player(); p2.name = 'Freddy'; p2.bank = 100; p2.bust = False; p2.hand = []; p2.bet1 = 0; p2.bet2 = 0; p2.boss = 2
p3 = Player(); p3.name = 'Kristo'; p3.bank = 100; p3.bust = False; p3.hand = []; p3.bet1 = 0; p3.bet2 = 0; p3.boss = 3
p4 = Player(); p4.name = 'Carlie'; p4.bank = 100; p4.bust = False; p4.hand = []; p4.bet1 = 0; p4.bet2 = 0; p4.boss = 4

# Add dealer to the players list and make a variable p holds the current player

players = [p0]
p = players[0]

# Card has 4 attributes: value, suit, color, name

class Card:
	def __init__(self):
		value = None; name = None; color = None; suit = None

ha = Card(); ha.value = 11; ha.suit = 'heart'; ha.color = 'red'; ha.name = 'A Heart'
h2 = Card(); h2.value = 2; h2.suit = 'heart'; h2.color = 'red'; h2.name = '2 Heart'
h3 = Card(); h3.value = 3; h3.suit = 'heart'; h3.color = 'red'; h3.name = '3 Heart'
h4 = Card(); h4.value = 4; h4.suit = 'heart'; h4.color = 'red'; h4.name = '4 Heart'
h5 = Card(); h5.value = 5; h5.suit = 'heart'; h5.color = 'red'; h5.name = '5 Heart'
h6 = Card(); h6.value = 6; h6.suit = 'heart'; h6.color = 'red'; h6.name = '6 Heart'
h7 = Card(); h7.value = 7; h7.suit = 'heart'; h7.color = 'red'; h7.name = '7 Heart'
h8 = Card(); h8.value = 8; h8.suit = 'heart'; h8.color = 'red'; h8.name = '8 Heart'
h9 = Card(); h9.value = 9; h9.suit = 'heart'; h9.color = 'red'; h9.name = '9 Heart'
h0 = Card(); h0.value = 10; h0.suit = 'heart'; h0.color = 'red'; h0.name = '10 Heart'
hj = Card(); hj.value = 10; hj.suit = 'heart'; hj.color = 'red'; hj.name = 'J Heart'
hq = Card(); hq.value = 10; hq.suit = 'heart'; hq.color = 'red'; hq.name = 'Q Heart'
hk = Card(); hk.value = 10; hk.suit = 'heart'; hk.color = 'red'; hk.name = 'K Heart'

da = Card(); da.value = 11; da.suit = 'diamond'; da.color = 'red'; da.name = 'A Dimond'
d2 = Card(); d2.value = 2; d2.suit = 'diamond'; d2.color = 'red'; d2.name = '2 Dimond'
d3 = Card(); d3.value = 3; d3.suit = 'diamond'; d3.color = 'red'; d3.name = '3 Dimond'
d4 = Card(); d4.value = 4; d4.suit = 'diamond'; d4.color = 'red'; d4.name = '4 Dimond'
d5 = Card(); d5.value = 5; d5.suit = 'diamond'; d5.color = 'red'; d5.name = '5 Dimond'
d6 = Card(); d6.value = 6; d6.suit = 'diamond'; d6.color = 'red'; d6.name = '6 Dimond'
d7 = Card(); d7.value = 7; d7.suit = 'diamond'; d7.color = 'red'; d7.name = '7 Dimond'
d8 = Card(); d8.value = 8; d8.suit = 'diamond'; d8.color = 'red'; d8.name = '8 Dimond'
d9 = Card(); d9.value = 9; d9.suit = 'diamond'; d9.color = 'red'; d9.name = '9 Dimond'
d0 = Card(); d0.value = 10; d0.suit = 'diamond'; d0.color = 'red'; d0.name = '10 Dimond'
dj = Card(); dj.value = 10; dj.suit = 'diamond'; dj.color = 'red'; dj.name = 'J Dimond'
dq = Card(); dq.value = 10; dq.suit = 'diamond'; dq.color = 'red'; dq.name = 'Q Dimond'
dk = Card(); dk.value = 10; dk.suit = 'diamond'; dk.color = 'red'; dk.name = 'K Dimond'

ca = Card(); ca.value = 11; ca.suit = 'club'; ca.color = 'black'; ca.name = 'A Club'
c2 = Card(); c2.value = 2; c2.suit = 'club'; c2.color = 'black'; c2.name = '2 Club'
c3 = Card(); c3.value = 3; c3.suit = 'club'; c3.color = 'black'; c3.name = '3 Club'
c4 = Card(); c4.value = 4; c4.suit = 'club'; c4.color = 'black'; c4.name = '4 Club'
c5 = Card(); c5.value = 5; c5.suit = 'club'; c5.color = 'black'; c5.name = '5 Club'
c6 = Card(); c6.value = 6; c6.suit = 'club'; c6.color = 'black'; c6.name = '6 Club'
c7 = Card(); c7.value = 7; c7.suit = 'club'; c7.color = 'black'; c7.name = '7 Club'
c8 = Card(); c8.value = 8; c8.suit = 'club'; c8.color = 'black'; c8.name = '8 Club'
c9 = Card(); c9.value = 9; c9.suit = 'club'; c9.color = 'black'; c9.name = '9 Club'
c0 = Card(); c0.value = 10; c0.suit = 'club'; c0.color = 'black'; c0.name = '10 Club'
cj = Card(); cj.value = 10; cj.suit = 'club'; cj.color = 'black'; cj.name = 'J Club'
cq = Card(); cq.value = 10; cq.suit = 'club'; cq.color = 'black'; cq.name = 'Q Club'
ck = Card(); ck.value = 10; ck.suit = 'club'; ck.color = 'black'; ck.name = 'K Club'

sa = Card(); sa.value = 11; sa.suit = 'spade'; sa.color = 'black'; sa.name = 'A Spade'
s2 = Card(); s2.value = 2; s2.suit = 'spade'; s2.color = 'black'; s2.name = '2 Spade'
s3 = Card(); s3.value = 3; s3.suit = 'spade'; s3.color = 'black'; s3.name = '3 Spade'
s4 = Card(); s4.value = 4; s4.suit = 'spade'; s4.color = 'black'; s4.name = '4 Spade'
s5 = Card(); s5.value = 5; s5.suit = 'spade'; s5.color = 'black'; s5.name = '5 Spade'
s6 = Card(); s6.value = 6; s6.suit = 'spade'; s6.color = 'black'; s6.name = '6 Spade'
s7 = Card(); s7.value = 7; s7.suit = 'spade'; s7.color = 'black'; s7.name = '7 Spade'
s8 = Card(); s8.value = 8; s8.suit = 'spade'; s8.color = 'black'; s8.name = '8 Spade'
s9 = Card(); s9.value = 9; s9.suit = 'spade'; s9.color = 'black'; s9.name = '9 Spade'
s0 = Card(); s0.value = 10; s0.suit = 'spade'; s0.color = 'black'; s0.name = '10 Spade'
sj = Card(); sj.value = 10; sj.suit = 'spade'; sj.color = 'black'; sj.name = 'J Spade'
sq = Card(); sq.value = 10; sq.suit = 'spade'; sq.color = 'black'; sq.name = 'Q Spade'
sk = Card(); sk.value = 10; sk.suit = 'spade'; sk.color = 'black'; sk.name = 'K Spade'

# Twenty decks of cards shuffled then concanated

d = [ha, h2, h3, h4, h5, h6, h7, h8, h9, h0, hj, hq, hk,
	da, d2, d3, d4, d5, d6, d7, d8, d9, d0, dj, dq, dk,
	ca, c2, c3, c4, c5, c6, c7, c8, c9, c0, cj, cq, ck,
	sa, s2, s3, s4, s5, s6, s7, s8, s9, s0, sj, sq, sk]
deck = []
for i in range (20):
	random.shuffle(d)
	for j in d:
		deck.append(j)

# Make variables: stage, counter, text_size, players_total, two lists of colors
pens = []
grfx = []
stage = 'adds'
counter = 0
text_size = 17
text_adj = 0
players_total = 1
bg_colors = ['#300600', '#300600', '#2e1700', '#2b2600', '#1a2b00', '#00290d',
		     '#042e1c', '#00062e', '#190136', '#360029', '#2b000a', '#1b003d']
fg_colors = ['#e9fc88', '#ffa200', '#fc7951', '#98fc51', '#64fa8e', '#6efff8',
		      '#65b3fc', '#36f582', '#d4cfff', '#ff7dda']
fg_color = fg_colors[random.randint(0, len(fg_colors) - 1)]
print(fg_color)
# Create the window interface and title graphics

wn = turtle.Screen()
wn.setup(480, 800)
wn.bgcolor(bg_colors[random.randint(0, len(bg_colors) - 1)])
wn.title(' ')
wn.tracer(0)

bj_title = turtle.Turtle()
bj_title.ht()
bj_title.penup()
bj_title.color(fg_color)
bj_title.goto(-210, 364)
bj_title.write('Blackjack', 
	align = 'left', font = ('Arial', text_size * 2, 'normal'))
grfx.append(bj_title)


for i in range(0, 3):
	temp = turtle.Turtle()
	temp.color(fg_color)
	temp.shape('square')
	temp.penup()
	grfx.append(temp)
	if i == 0:
		temp.shapesize(0.01, 24)
		temp.goto(0, 360)
	if i == 1:
		temp.shapesize(0.01, 24)
		temp.goto(0, 80)
	if i == 2:
		temp.shapesize(14, 0.01)
		temp.goto(-50, 220)

# Create the turtle pens to write the options, hands, outcomes

out = turtle.Turtle()
out.ht()
out.penup()
out.color(fg_color)
out.goto(-30, 100)
out.write('How Many Players?\n\n(1)    (2)    (3)     (4)', 
	align = 'left', font = ('Arial', text_size + text_adj, 'normal'))
grfx.append(out)



for i in range(0, len(players)):
	pen = turtle.Turtle()
	pen.ht()
	pen.penup()
	pen.color(fg_color)
	if i == 0:
		pen.goto(-180, 100)
		pen.write('',
			align = 'left', font = ('Arial', text_size, 'normal'))
	else:
		pen.goto(-320 + i * 94, -140)
		pen.write('',
			align = 'left', font = ('Arial', text_size, 'normal'))
	pens.append(pen)
	grfx.append(pen)

def update_pens(a):
	for i in pens:
		i.clear()

	# Write each player's info: s = cards, b = bust, x = total

	for i in range(0, len(players)):
		s = b = bet_amount = up = ''
		x = 0
		if p == players[i]:
			up = '*\n'

		# Get every player's count, make a string to hold player info

		for j in range(0, len(players[i].hand)):
			x = x + players[i].hand[j].value
			s = s + '\n' + str(players[i].hand[j].name)

		# If player is over 21, update player as bust = true

		if players[i].bust == True:
			b = '* B U S T *\n'

		# If this is a player's second hand, hide bank amount.

		if players[i].bank > 0:
			bet_amount = '\n$' + str(players[i].bank)

		# Pen placement for dealer

		if i == 0:
			pen.goto(-180, 100)
			
			# Write dealer's name, cards (s), total (x), and if busted (b)

			if a.name == 'Dealer':
				pen.write(up + b + players[i].name + s + '\n---\n' + str(x),
					align = 'left', font = ('Arial', text_size, 'normal'))

			# Write dealer's info but hide first card and score

			else:
				s = ''

				for j in range(0, len(players[i].hand)):
					if j == 0:
						s = s + '\n' + 'x'
					else:
						s = s + '\n' + str(players[i].hand[j].name)

				# Check to see if the dealer has cards or not

				if x > 0:
					pen.write(up + b + players[i].name + s,
					align = 'left', font = ('Arial', text_size, 'normal'))

				else: 
					pen.write(players[i].name,
					align = 'left', font = ('Arial', text_size, 'normal'))

		# Place player data in a row

		elif 0 < i < 6:
			pen.goto(-320 + i * 94, -140)

			ins = ''

			if players[i].bet2 > 0:
				ins = '\nCover: ' + str(players[i].bet2)
				print(ins)

			# Write each player's name, bet amount, cards, total, and bust status

			if x > 0:
				pen.write(up + b + players[i].name + bet_amount + ins + '\nBet: ' + 
					str(players[i].bet1) + s + '\n---\n' + str(x),
					align = 'left', font = ('Arial', text_size, 'normal'))

			# Do not write player count if there are no cards dealt.

			else:
				pen.write(players[i].name + bet_amount + '\nBet: ' + 
					str(players[i].bet1),
					align = 'left', font = ('Arial', text_size, 'normal'))

		else:
			pen.goto(-790 + i * 94, -380)

			ins = ''

			if players[i].bet2 > 0:
				ins = '\nCover: ' + str(players[i].bet2)
				print(ins)

			# Write each player's name, bet amount, cards, total, and bust status

			if x > 0:
				pen.write(up + b + players[i].name + bet_amount + ins +
					'\nBet: ' + str(players[i].bet1)
					 + s + '\n---\n' + str(x),
					align = 'left', font = ('Arial', text_size, 'normal'))

			# Do not write player count if there are no cards dealt.

			else:
				pen.write(players[i].name + bet_amount + 
					'\nBet: ' + str(players[i].bet1),
					align = 'left', font = ('Arial', text_size, 'normal'))


# Handle asking each player if they want insurance

def handle_insurance(a):

	# Clear the pens

	for i in pens:
		i.clear()
	
	# Write each player's info using this for loop

	for i in range(0, len(players)):

		# Make some variables to hold info. s = cards, b = bust, x = total

		s = up = ''
		x = 0
		
		# Get player counts and cards

		for j in range(0, len(players[i].hand)):
			x = x + players[i].hand[j].value
			s = s + '\n' + str(players[i].hand[j].name)
			if p == players[i]:
				up = '*\n'

		# Special pen placement for dealer

		if i == 0:
			pen.goto(-180, 100)

			# Write dealer's info but hide first card and score

			s = ''
			for j in range(0, len(players[i].hand)):
				if j == 0:
					s = s + '\n' + 'x'
				else:
					s = s + '\n' + str(players[i].hand[j].name)

			pen.write(up + players[i].name + s,
				align = 'left', font = ('Arial', text_size, 'normal'))

		elif 0 < i < 6:
			pen.goto(-320 + i * 94, -140)

			# Write each player's name, bet amount, cards, total, and bust status

			if players[i] == a:

				pen.write(up + players[i].name + '\n$' + str(players[i].bank) + 
					'\nBet: ' + str(players[i].bet1)
					+ s + '\n---\n' + str(x) + '\n' + '\nCover?\nY or N',
					align = 'left', font = ('Arial', text_size, 'normal'))

			else:
				ins = ''
				if players[i].bet2 > 0:
					ins = '\nCover: ' + str(players[i].bet2)

				pen.write(up + players[i].name + '\n$' + str(players[i].bank) + ins +
					'\nBet: ' + str(players[i].bet1)
					+ s + '\n---\n' + str(x),
					align = 'left', font = ('Arial', text_size, 'normal'))

		else:
			pen.goto(-790 + i * 94, -380)

			# Write each player's name, bet amount, cards, total, and bust status

			if players[i] == a:

				pen.write(up + players[i].name + '\n$' + str(players[i].bank) + 
					'\nBet: ' + str(players[i].bet1)
					+ s + '\n---\n' + str(x) + '\n' + '\nCover?\nY or N',
					align = 'left', font = ('Arial', text_size, 'normal'))

			else:

				ins = ''
				if players[i].bet2 > 0:
					ins = '\nCover: ' + str(players[i].bet2)
					print(ins)

				pen.write(up + players[i].name + '\n$' + str(players[i].bank) + ins +
					'\nBet: ' + str(players[i].bet1)
					+ s + '\n---\n' + str(x),
					align = 'left', font = ('Arial', text_size, 'normal'))

# Calculate the player's count

def get_count(a):
	x = 0
	for i in a.hand:
		x = x + i.value
	return (x)

# Call this after all the players have finished

def dealers_turn():
	global p
	global stage
	global players
	global players_count
	

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
			s = []
			counts = []

			for i in players:
				players_count = 0

				for j in i.hand:
					players_count = players_count + j.value
				counts.append(players_count)
				s.append('')

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
							players[players[i].boss].bank = players[players[i].boss].bank + players[i].bet1 * 2

						# Or else it's a tie

						else:
							s[i] = players[i].name + ' and Dealer push.'
							players[players[i].boss].bank = players[players[i].boss].bank + players[i].bet1

						# Handle natural blackjack

						if len(players[i].hand) == 2 and counts[i] == 21:
							s[i] = s[i] + ' Natural!'
							players[players[i].boss].bank = players[players[i].boss].bank + int(players[i].bet1 * 0.5)

					# Settle security

					if x == 21 and len(p.hand) == 2:
						if players[i].bet2 > 0:
							players[players[i].boss].bank = players[players[i].boss].bank + players[i].bet2
							s[i] = s[i] + str(players[i].bet2) + ' recovered.'

			# Dealer is over 21 and busts

			else:
				p.bust = True

				for i in range(1, len(players)):
					if players[i].bust == False:
						s[i] = players[i].name + ' beats Dealer.'

						# Handle natural blackjack

						if len(players[i].hand) == 2 and counts[i] == 21:
							s[i] = s[i] + ' Natural!'
							players[players[i].boss].bank = players[players[i].boss].bank + int(players[i].bet1 * 0.5)

						players[players[i].boss].bank = players[players[i].boss].bank + players[i].bet1 * 2

					else:
						s[i] = players[i].name + ' busts.'

			# Combine all the strings into one and put it in out_text

			out_text = ''
			for i in s:
				out_text = out_text + '\n' + i
			out_text = out_text + '\n\n(A)gain?'
			out.clear()
			out.write(out_text, align = 'left', font = ('Arial', text_size + text_adj, 'normal'))

			update_pens(p)
			break

# Cycle through player turns

def change_players():
	global p
	global players

	i = players.index(p)

	if i == len(players) - 1:
		p = players[0]
		dealers_turn()
		
	else:
		p = players[i + 1]

# Display various outcomes and update stage

def show_hit_or_pass():
	global p
	global stage

	stage = 'hit or pass'
	out.clear()
	out.write(p.name + "'s Turn\n(H)it or (P)ass", 
		align = 'left', font = ('Arial', text_size + text_adj, 'normal'))

def show_insurance():
	global p
	global stage

	stage = 'insurance'
	out.clear()
	out.write(p.name + "'s Turn\nDealer has an ace.", 
		align = 'left', font = ('Arial', text_size + text_adj, 'normal'))

def show_double():
	global p
	global stage

	stage = 'double'
	out.clear()
	out.write(p.name + "'s Turn\nTotal 9, 10, or 11\nDouble Down?\n(Y)es or (N)o", 
		align = 'left', font = ('Arial', text_size + text_adj, 'normal'))

def show_split():
	global p
	global stage

	stage = 'split'
	out.clear()
	out.write(p.name + "'s Turn\nSplit Pair?\n(Y)es or (N)o", 
		align = 'left', font = ('Arial', text_size + text_adj, 'normal'))

def show_betting():
	global p
	global stage

	stage = 'bets'
	out.clear()
	out.write(p.name + "'s Turn\nPlace Bets\n_______\n\n" + 
		'(1)  $10\n\n(2)  $20\n\n(3)  $30\n\n(4)  $40', 
		align = 'left', font = ('Arial', text_size + text_adj, 'normal'))

# Write the betting amounts

def start_place_bets():
	global p
	global stage
	global players

	p = players[1]
	show_betting()
	update_pens(p)
	
# Place bets

def next_bet():
	global p
	global stage
	global players

	i = players.index(p)

	if i == len(players) - 1:
		p = players[1]
		out.clear()
		out.write('(D)eal', align = 'left', font = ('Arial', text_size + text_adj, 'normal'))
		stage = 'deal'
	else:
		p = players[i + 1]
		show_betting()

# Reset game

def press_d():
	global p
	global stage
	global players

	if stage == 'deal':

		# Set everyone's bust to false, empty all hands, place all bets

		for i in players:
			i.bust = False
			i.hand = []
			i.bet2 = 0
			i.bank = i.bank - i.bet1

		# Deal two cards to all players

		for i in range(0, 2):
			for i in players:
				i.hand.append(deck[-1])
				deck.pop()

		# Use a variable, p, to hold the current player

		p = players[1]

		# If dealer's second card is an ace, offer insurance to players

		if players[0].hand[1].value == 11:
			show_insurance()
			handle_insurance(p)
			
		# Clear previous outcome and update pens

		else:
			if 8 < p.hand[0].value + p.hand[1].value < 12:
				show_double()

			elif len(p.hand) == 2:
				if p.hand[0].value == p.hand[1].value:
					show_split()
				else:
					show_hit_or_pass()
			else:
				show_hit_or_pass()

			update_pens(p)

# Function to add a card to the current player

def press_h():
	global p
	global stage
	global players

	if stage == 'hit or pass':

		# Current player draws a card from the deck

		p.hand.append(deck[-1])
		deck.pop()

		# Get the player's count

		x = get_count(p)

		# If player has two cards and they are equal, offer split

		if len(p.hand) == 2:
			if p.hand[0].value == p.hand[1].value:
				show_split()
			else:
				show_hit_or_pass()
		else:
			show_hit_or_pass()

		# If player busts with an ace, set the ace equal to one

		for i in range(len(p.hand)):
			if p.hand[i].value == 11 and x > 21:
				p.hand[i].value = 1
				break

		x = get_count(p)

		# If player's count is over 21, change player

		if x > 21:
			p.bust = True

			change_players()

			if p != players[0]:

				if 8 < p.hand[0].value + p.hand[1].value < 12:
					show_double()
				elif len(p.hand) == 2:
					if p.hand[0].value == p.hand[1].value:
						show_split()
					else:
						show_hit_or_pass()
				else:
					show_hit_or_pass()

		update_pens(p)

# Change to the next player

def press_p():
	global p
	global stage
	global players

	if stage == 'hit or pass':
		change_players()

		if p != players[0]:

			if 8 < p.hand[0].value + p.hand[1].value < 12:
				show_double()
			elif len(p.hand) == 2:
				if p.hand[0].value == p.hand[1].value:
					show_split()
				else:
					show_hit_or_pass()
			else:
				show_hit_or_pass()

		update_pens(p)

# User input for bet amounts

def press_1():
	global p
	global stage
	global players
	global players_total

	if stage == 'bets':
		p.bet1 = 10
		update_pens(p)
		if p != players[0]:
			next_bet()
		
	if stage == 'adds':
		players = [p0, p1]
		players_total = 1
		p = players[1]
		start_place_bets()

def press_2():
	global p
	global stage
	global players
	global players_total

	if stage == 'bets' and p.bank >= 20:
		p.bet1 = 20
		update_pens(p)
		if p != players[0]:
			next_bet()

	if stage == 'adds':
		players = [p0, p1, p2]
		players_total = 2
		start_place_bets()

def press_3():
	global p
	global stage
	global players
	global players_total

	if stage == 'bets' and p.bank >= 30:
		p.bet1 = 30
		update_pens(p)
		if p != players[0]:
			next_bet()

	if stage == 'adds':
		players = [p0, p1, p2, p3]
		players_total = 3
		start_place_bets()

def press_4():
	global p
	global stage
	global players
	global players_total

	if stage == 'bets' and p.bank >= 40:
		p.bet1 = 40
		update_pens(p)
		if p != players[0]:
			next_bet()
		
	if stage == 'adds':
		players = [p0, p1, p2, p3, p4]
		players_total = 4
		start_place_bets()

def press_y():
	global p
	global stage
	global players

	if stage == 'double':
		players[p.boss].bank = players[p.boss].bank - p.bet1
		p.bet1 = p.bet1 * 2

		show_hit_or_pass()
		update_pens(p)

	if stage == 'split':
		pX = Player(); pX.name = p.name + '+'; pX.bank = 0; pX.bust = False
		pX.hand = []; pX.bet1 = p.bet1; pX.bet2 = 0; pX.boss = p.boss
		p.bank = p.bank - p.bet1
		pX.hand.append(p.hand[-1])
		p.hand.pop()

		# Get player's turn position and add insert a new player right after

		i = players.index(p)
		players.insert(i + 1, pX)

		# Add a card to the current player and player's split hand

		players[i].hand.append(deck[-1])
		deck.pop()
		players[i + 1].hand.append(deck[-1])
		deck.pop()

		if 8 < p.hand[0].value + p.hand[1].value < 12:
			show_double()
		elif len(p.hand) == 2:
			if p.hand[0].value == p.hand[1].value:
				show_split()
			else:
				show_hit_or_pass()
		else:
			show_hit_or_pass()
		update_pens(p)

	if stage == 'insurance':
		p.bet2 = int(p.bet1 * 0.5)
		p.bank = p.bank - p.bet2

		i = players.index(p)
		if i == len(players) - 1:
			p = players[1]

			if 8 < p.hand[0].value + p.hand[1].value < 12:
				show_double()
			elif len(p.hand) == 2:
				if p.hand[0].value == p.hand[1].value:
					show_split()
				else:
					show_hit_or_pass()
			else:
				show_hit_or_pass()
			update_pens(p)

		else:
			p = players[i + 1]
			handle_insurance(p)

def press_n():
	global p
	global stage
	global players
	
	if stage == 'insurance':
		i = players.index(p)

		if i == len(players) - 1:
			p = players[1]
			show_hit_or_pass()
			update_pens(p)
		else:
			p = players[i + 1]
			handle_insurance(p)

	if stage == 'split':
		show_hit_or_pass()
		update_pens(p)

	if stage == 'double':
		if p.hand[0].value == p.hand[1].value:
			show_split()
		else:
			show_hit_or_pass()
		update_pens(p)

def press_a():
	global p
	global stage
	global players
	global players_total

	if stage == 'start':
		wn.bgcolor(bg_colors[random.randint(0, len(bg_colors) - 1)])

		# Set everyone's bust to false, empty hands and bets

		for i in players:
			i.bust = False
			i.hand = []
			i.bet1 = 0
			i.bet2 = 0
			i.bank = i.bank - i.bet1

		# Remove the split pairs hands

		if players_total == 4:
			players = [p0, p1, p2, p3, p4]
		if players_total == 3:
			players = [p0, p1, p2, p3]
		if players_total == 2:
			players = [p0, p1, p2]
		if players_total == 1:
			players = [p0, p1]

		# Remove players with no money

		for i in players:
			if i.bank <= 0:
				players.remove(i)

		# Reset player's boss numbers because players are removed

		for i in range (0, len(players)):
			players[i].boss = i

		p = players[1]

		show_betting()
		update_pens(p)
		
# Hook functions up with heys on the keyboard

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
turtle.onkey(press_a, 'a')

while True:
	wn.update()

	counter = counter + 1
	if counter % 10000 == 0:
		print(p.name)
		print(stage)
		print(players_total)

