# Magic 8 ball made to top Trimble.
# Made for python 3
from random import randint

i = input('What is thy query? ')
o = randint(1, 20)

if o == 1:
	print('It is certain so.')
if o == 2:
	print('It is decidedly so.')
if o == 3:
	print('Without a doubt.')
if o == 4:
	print('Yes, definately.')
if o == 5:
	print('You may rely on it.')
if o == 6:
	print('As I see it, yes.')
if o == 7:
	print('Most likely.')
if o == 8:
	print('Outlook good.')
if o == 9:
	print('Yes.')
if o == 10:
	print('Signs point to yes.')
if o == 11:
	print('Reply hazy, try again.')
if o == 12:
	print('Ask again later.')
if o == 13:
	print('Better not tell you now.')
if o == 14:
	print('Cannot predict now.')
if o == 15:
	print('Concentrate and ask again.')
if o == 16:
	print('Don\'t count on it.')
if o == 17:
	print('My reply is no.')
if o == 18:
	print('My sources say no.')
if o == 19:
	print('Outlook not so good.')
if o == 20:
	print('Very doubtful.')

input('\nPress any enter to exit.')
