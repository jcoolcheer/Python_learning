print('hello world')
#this is a comment

print('hello zee\nnice to meet you!')
#hello zee
# nice to meet you

print(r'hello zee\nnice to meet you!')
# hello zee nice to meet you!

print('what\'s your name?''i\'m zee')
# what's your name ? i'm zee auto automatic


i = 5
print (i)
# 5
i= i+1
print (i)
# 6

sentence = 'this is a demo text'
print (sentence)

long_s = 'this is a very long \
sentence.'
print (long_s)
# this is a very long sentence.

number = 23
in_int = int(input('enter a number: '))
if in_int == number:
	print ('yes,the same!')
elif in_int < number:
	print ('in_int is smaller than number')
else:
	print ('in_int is bigger than number')
running = True
#capitalize

while running:
	usr_input = int(input('please input a number: '))
	if usr_input > 0:
		print ('wow,it\'s bigger than 0')
		running = False
	elif usr_input == 0:
		print ('wow,it\'s equal to 0')
	else:
		print ('wow,it\'s smaller than 0')
# print ('done!')

for i in range(1,10):
	print(i)
#1,2,3,4,5,6,7,8,9

run = True
while run: 
	s = input('please enter a string: ')
	if s == 'quit':
		break
	if len(s) < 3:
		continue
	print ('hello ,can you see me?')
print ('done')

#----------------FUNCTION------------

def sayHello():
	print ('hello zee')


sayHello()



def change_num(x):
	print('now x is: ',x)
	x = 22
	print ('but now ,x is: ',x)
x = 50
change_num(x)
print ('finally, x is: ',x)

def say_times(name,times = 1):
	print (name*times)

say_times('zee')
say_times('zee',7)

def numbers(x,y):
	"""This is a how to say.

	a a a natural content"""
	if x > y:
		print ('yes ',x,'is bigger than',y)
	else:
		print ('forget it')
numbers(10,9)
print (numbers.__doc__)