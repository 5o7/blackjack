import turtle
import random

class Card:
	def __init__(self):
		num = None
		name = None
		color = None
		suit = None

xx = Card(); xx.num = 0; xx.name = 'x'
ha = Card(); ha.num = 1; ha.name = 'Ace of Hearts'
h2 = Card(); h2.num = 2; h2.name = 'Two of Hearts'
h3 = Card(); h3.num = 3; h3.name = 'Three of Hearts'
h4 = Card(); h4.num = 4; h4.name = 'Four of Hearts'
h5 = Card(); h5.num = 5; h5.name = 'Five of Hearts'
h6 = Card(); h6.num = 6; h6.name = 'Six of Hearts'
h7 = Card(); h7.num = 7; h7.name = 'Seven of Hearts'
h8 = Card(); h8.num = 8; h8.name = 'Eight of Hearts'
h9 = Card(); h9.num = 9; h9.name = 'Nine of Hearts'
h0 = Card(); h0.num = 10; h0.name = 'Ten of Hearts'
hj = Card(); hj.num = 10; hj.name = 'Jack of Hearts'
hq = Card(); hq.num = 10; hq.name = 'Queen of Hearts'
hk = Card(); hk.num = 10; hk.name = 'King of Hearts'
da = Card(); da.num = 1; da.name = 'Ace of Diamonds'
d2 = Card(); d2.num = 2; d2.name = 'Two of Diamonds'
d3 = Card(); d3.num = 3; d3.name = 'Three of Diamonds'
d4 = Card(); d4.num = 4; d4.name = 'Four of Diamonds'
d5 = Card(); d5.num = 5; d5.name = 'Five of Diamonds'
d6 = Card(); d6.num = 6; d6.name = 'Six of Diamonds'
d7 = Card(); d7.num = 7; d7.name = 'Seven of Diamonds'
d8 = Card(); d8.num = 8; d8.name = 'Eight of Diamonds'
d9 = Card(); d9.num = 9; d9.name = 'Nine of Diamonds'
d0 = Card(); d0.num = 10; d0.name = 'Ten of Diamonds'
dj = Card(); dj.num = 10; dj.name = 'Jack of Diamonds'
dq = Card(); dq.num = 10; dq.name = 'Queen of Diamonds'
dk = Card(); dk.num = 10; dk.name = 'King of Diamonds'
ca = Card(); ca.num = 1; ca.name = 'Ace of Clubs'
c2 = Card(); c2.num = 2; c2.name = 'Two of Clubs'
c3 = Card(); c3.num = 3; c3.name = 'Three of Clubs'
c4 = Card(); c4.num = 4; c4.name = 'Four of Clubs'
c5 = Card(); c5.num = 5; c5.name = 'Five of Clubs'
c6 = Card(); c6.num = 6; c6.name = 'Six of Clubs'
c7 = Card(); c7.num = 7; c7.name = 'Seven of Clubs'
c8 = Card(); c8.num = 8; c8.name = 'Eight of Clubs'
c9 = Card(); c9.num = 9; c9.name = 'Nine of Clubs'
c0 = Card(); c0.num = 10; c0.name = 'Ten of Clubs'
cj = Card(); cj.num = 10; cj.name = 'Jack of Clubs'
cq = Card(); cq.num = 10; cq.name = 'Queen of Clubs'
ck = Card(); ck.num = 10; ck.name = 'King of Clubs'
sa = Card(); sa.num = 1; sa.name = 'Ace of Spades'
s2 = Card(); s2.num = 2; s2.name = 'Two of Spades'
s3 = Card(); s3.num = 3; s3.name = 'Three of Spades'
s4 = Card(); s4.num = 4; s4.name = 'Four of Spades'
s5 = Card(); s5.num = 5; s5.name = 'Five of Spades'
s6 = Card(); s6.num = 6; s6.name = 'Six of Spades'
s7 = Card(); s7.num = 7; s7.name = 'Seven of Spades'
s8 = Card(); s8.num = 8; s8.name = 'Eight of Spades'
s9 = Card(); s9.num = 9; s9.name = 'Nine of Spades'
s0 = Card(); s0.num = 10; s0.name = 'Ten of Spades'
sj = Card(); sj.num = 10; sj.name = 'Jack of Spades'
sq = Card(); sq.num = 10; sq.name = 'Queen of Spades'
sk = Card(); sk.num = 10; sk.name = 'King of Spades'

deck = [ha, h2, h3, h4, h5, h6, h7, h8, h9, h0, hj, hq, hk,
		da, d2, d3, d4, d5, d6, d7, d8, d9, d0, dj, dq, dk,
		ca, c2, c3, c4, c5, c6, c7, c8, c9, c0, cj, cq, ck,
		sa, s2, s3, s4, s5, s6, s7, s8, s9, s0, sj, sq, sk]

p2 = []
p1a = []
p1b = []
p1c = []
toss = []
stage = 'pregame'
counter = 0
bank = 500
bet = 10

wn = turtle.Screen()
wn.setup(480, 820)
wn.tracer(0)

rules = turtle.Turtle()
rules.ht()
rules.penup()
rules.goto(-230, 200)
rules.write('BLACKJACK\n\nRules:\n(R)eset\n(D)eal\n' + 
	'(S)plit\n(H)it\n(P)ass\n(2)Double\n(Q)uit', 
	align = 'left', font = ('Symbol', 18, 'normal'))

score = turtle.Turtle()
score.ht()
score.penup()
score.goto(-100, -200)
score.write('Press (R) to Reset\n\nYou have $' + str(bank), 
	align = 'left', font = ('Symbol', 18, 'normal'))

def quit_game():
	print('Program quit successfully.')
	turtle.mainloop()

def list_cards(a, b, c, d):
	string1 = string2 = string3 = string0 = ''
	for i in a:
		string1 = string1 + '\n' + i.name
	for i in b:
		string2 = string2 + '\n' + i.name
	for i in c:
		string3 = string3 + '\n' + i.name
	for i in d:
		string0 = string0 + '\n' + i.name
	return(string1, string2, string3, string0)

def check_count(a, b, c, d):
	_x1a = _x1b = _x1c = _x2 = 0
	for i in a:
		_x1a = _x1a + i.num
	for i in b:
		_x1b = _x1b + i.num
	for i in c:
		_x1c = _x1c + i.num
	for i in d:
		_x2 = _x2 + i.num
	return(_x1a, _x1b, _x1c, _x2)

def print_cards(bank, bet, p1a, p1b, p1c, p2, stage):

	s1, s2, s3, s0 = list_cards(p1a, p1b, p1c, p2)
	x1a, x1b, x1c, x2 = check_count(p1a, p1b, p1c, p2)

	if len(p1c) > 0:
		score.clear()
		score.write('Player One cards:' + s1 + '\n' + str(x1a) + 
			'\n\nSplit One cards:' + s2 + '\n' + str(x1b) + 
			'\n\nSplit Two cards:' + s3 +  '\n' + str(x1c) + 
			'\n\nDealear has: ' + s0 + str(x2) + 
			'\n\nYou have $' + str(bank), 
			align = 'left', font = ('Courier', 18, 'normal'))

	elif len(p1b) > 0:
		score.clear()
		score.write('Player One cards:' + s1 + '\n' + str(x1a) + 
			'\n\nSplit One cards:' + s2 + '\n' + str(x1b) + 
			'\n\nDealear has: ' + s0 +  '\n' + str(x2) + 
			'\n\nYou have $' + str(bank), 
			align = 'left', font = ('Courier', 18, 'normal'))

	else:
		score.clear()
		score.write('Player One cards:' + s1 + '\n' + str(x1a) + 
			'\n\nDealear has: ' + s0 + '\n' + str(x2) + 
			'\n\nYou have $' + str(bank), 
			align = 'left', font = ('Courier', 18, 'normal'))

def reset_game():
	global p1a, p1b, p1c, p2, toss, stage, bank, bet

	for i in p1a:
		deck.append(p1a[-1])
		p1a.pop()
	for i in p1b:
		deck.append(p1b[-1])
		p1b.pop()
	for i in p1c:
		deck.append(p1c[-1])
		p1c.pop()
	for i in p2:
		deck.append(p2[-1])
		p2.pop()
	for i in toss:
		deck.append(toss[-1])
		toss.pop()

	random.shuffle(deck)

	p2 = []
	p1a = []
	p1b = [] 
	p1c = []
	toss = []
	stage = 'pregame'
	bank = 200
	bet = 10
	
	score.clear()
	score.write('Game has been reset.\n\nYou have $' + str(bank), 
		align = 'left', font = ('Symbol', 18, 'normal'))

def deal():
	global p1a, p1b, p1c, p2, toss, stage, bank, bet

	if stage == 'pregame':
		for i in p1a:
			toss.append(p1a[-1])
			p1a.pop()
		for i in p1b:
			toss.append(p1b[-1])
			p1b.pop()
		for i in p1c:
			toss.append(p1c[-1])
			p1c.pop()
		for i in p2:
			toss.append(p2[-1])
			p2.pop()

		p1a = []
		p1b = []
		p1c = []
		p2 = []
		
		bank = bank - bet
		for i in range(0, 2):
			p1a.append(deck[-1])
			deck.pop()
			p2.append(deck[-1])
			deck.pop()

		stage = 'stack1'

		print_cards(bank, bet, p1a, p1b, p1c, p2, stage)

def hit():
	global p1a, p1b, p1c, p2, toss, stage, bank, bet

	if stage == 'stack1':
		p1a.append(deck[-1])
		deck.pop()
		print_cards(bank, bet, p1a, p1b, p1c, p2, stage)

	if stage == 'stack2':
		p1b.append(deck[-1])
		deck.pop()
		print_cards(bank, bet, p1a, p1b, p1c, p2, stage)

	if stage == 'stack3':
		p1c.append(deck[-1])
		deck.pop()
		print_cards(bank, bet, p1a, p1b, p1c, p2, stage)



def pass_turn():
	global p1a, p1b, p1c, p2, toss, stage, bank, bet

	if stage == 'stack3':
		stage = 'vs3'

	if stage == 'stack2':
		if len(p1c) == 0:
			stage = 'vs2'
		else:
			stage = 'stack3'

	if stage == 'stack1':
		if len(p1b) == 0:
			stage = 'vs1'
		else:
			stage = 'stack2'

def split():
	global p1a, p1b, p1c, p2, toss, stage, bank, bet

	x1a, x1b, x1c, x2 = check_count(p1a, p1b, p1c, p2)

	if stage == 'stack1':
		if x1a == 20 and len(p1a) == 2:
			p1b.append(p1a[-1])
			p1a.pop()
			bank = bank - bet
			print_cards(bank, bet, p1a, p1b, p1c, p2, stage)

	if stage == 'stack2':
		if x1b == 20 and len(p1a) == 2:
			p1c.append(p1b[-1])
			p1b.pop()
			bank = bank - bet
			print_cards(bank, bet, p1a, p1b, p1c, p2, stage)

turtle.listen()
turtle.onkey(quit_game, 'q')
turtle.onkey(reset_game, 'r')
turtle.onkey(deal, 'd')
turtle.onkey(hit, 'h')
turtle.onkey(pass_turn, 'p')
turtle.onkey(split, 's')

while True:
	wn.update()

	counter = counter + 1
	if counter % 10000 == 0:
		print(stage)

	# Dealer's turn up against one hand

	if stage == 'vs1':

		while True:

			# Get the counts

			x1a, x1b, x1c, x2 = check_count(p1a, p1b, p1c, p2)
			s1, s2, s3, s0 = list_cards(p1a, p1b, p1c, p2)

			# Dealer will draw cards until count is more than 16

			if x2 < 17:
				p2.append(deck[-1])
				deck.pop()

			else:

				# Check if dealer busts

				if x2 > 21:
					bank = bank + bet * 2
					score.clear()
					score.write('DEALER BUSTS. YOU WON!\n\n' + 
						'(R)eset or (D)eal a new hand.\n\n' +
						'Player One cards:' + s1 + '\n' + str(x1a) + 
						'\n\nDealear has: ' + s0 + '\n' + str(x2) + 
						'\n\nYou have $' + str(bank), 
						align = 'left', font = ('Courier', 18, 'normal'))
				else:

					# Check who won

					if x1a > x2:
						result = 'YOU WON!'
						bank = bank + bet * 2
					elif x2 > x1a:
						result = 'YOU LOST.'
					else:
						result = 'PUSH'
						bank = bank + bet

					score.clear()
					score.write(result + '\n\n(R)eset or (D)eal a new hand.' + 
						'\n\nPlayer One cards:' + s1 + '\n' + str(x1a) + 
						'\n\nDealear has: ' + s0 + '\n' + str(x2) + 
						'\n\nYou have $' + str(bank), 
						align = 'left', font = ('Courier', 18, 'normal'))
					
				stage = 'pregame'
				break

	if stage == 'vs2':

		# Get the counts

		x1a, x1b, x1c, x2 = check_count(p1a, p1b, p1c, p2)

		# Dealer will draw cards until count is more than 16

		if x2 < 17:
			p2.append(deck[-1])
			deck.pop()

		else:

			# Check if dealer busts

			if x2 > 21:
				bank = bank + bet * 4
				score.clear()
				score.write('DEALER BUSTS. YOU WON!\n' + 
					'(R)eset or (D)eal a new hand.\n' +
					'Player One cards:' + s1 + '\n' + str(x1a) + 
					'\n\nDealear has: ' + s0 + '\n' + str(x2) + 
					'\n\nYou have $' + str(bank), 
					align = 'left', font = ('Courier', 18, 'normal'))

			else:

				# Check who won

				if x1a > x2 and x1b > x2:
					result = 'YOU WON DOUBLE!'
					bank = bank + bet * 4
				elif x2 > x1a and x2 > x1b:
					result = 'YOU LOST DOUBLE.'
					bank = bank - bet * 4
				else:
					result = 'PUSH'
					bank = bank + bet

				s1, s2, s3, s0 = list_cards(p1a, p1b, p1c, p2)

				score.clear()
				score.write(result + '\n\n(R)eset or (D)eal a new hand.' + 
					'\n\nPlayer One cards:' + s1 + '\n' + str(x1a) + 
					'\n\nSplit One cards:' + s2 + '\n' + str(x1b) + 
					'\n\nDealear has: ' + s0 + '\n' + str(x2) + 
					'\n\nYou have $' + str(bank), 
					align = 'left', font = ('Courier', 18, 'normal'))
				
			stage = 'pregame'
			brerak

	if stage == 'vs3':

		# Get the counts

		x1a, x1b, x1c, x2 = check_count(p1a, p1b, p1c, p2)

		# Dealer will draw cards until count is more than 16

		if x2 < 17:
			p2.append(deck[-1])
			deck.pop()

		else:

			# Check if dealer busts

			if x2 > 21:
				bank = bank + bet * 6
				score.clear()
				score.write('DEALER BUSTS. YOU WON!\n' + 
					'(R)eset or (D)eal a new hand.\n' +
					'Player One cards:' + s1 + '\n' + str(x1a) + 
					'\n\nDealear has: ' + s0 + '\n' + str(x2) + 
					'\n\nYou have $' + str(bank), 
					align = 'left', font = ('Courier', 18, 'normal'))

			else:

				# Check who won

				if x1a > x2 and x1b > x2 and x1c > x2:
					result = 'YOU WON TRIPLE!'
					bank = bank + bet * 6
				elif x2 > x1a and x2 > x1b and x2> x1c:
					result = 'YOU LOST TRIPLE'
					bank = bank - bet * 6
				elif x1a > x2 and x1b > x2 and x1c < x2:
					result = 'YOU WON'
					bank = bank + bet * 4
				elif x1a > x2 and x1b < x2 and x1c > x2:
					result = 'YOU WON'
					bank = bank + bet * 4
				elif x1a < x2 and x1b > x2 and x1c > x2:
					result = 'YOU WON'
					bank = bank + bet * 4
				elif x1a > x2 and x1b < x2 and x1c < x2:
					result = 'YOU LOST'
					bank = bank - bet
				elif x1a < x2 and x1b > x2 and x1c < x2:
					result = 'YOU LOST'
					bank = bank - bet
				elif x1a < x2 and x1b < x2 and x1c > x2:
					result = 'YOU LOST'
					bank = bank - bet
				else:
					result = 'PUSH. This cannot happen.'
					bank = bank + bet

				s1, s2, s3, s0 = list_cards(p1a, p1b, p1c, p2)

				score.clear()
				score.write(result + '\n\n(R)eset or (D)eal a new hand.' + 
					'\n\nPlayer One cards:' + s1 + '\n' + str(x1a) + 
					'\n\nSplit One cards:' + s2 + str(x1b) + 
					'\n\nSplit Two cards:' + s3 + '\n' + str(x1c) + 
					'\n\nDealear has: ' + s0 + '\n' + str(x2) + 
					'\n\nYou have $' + str(bank), 
					align = 'left', font = ('Courier', 18, 'normal'))
				
			stage = 'pregame'
			break






