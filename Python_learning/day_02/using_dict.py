add = {
	'zee': 'zee@niuco.com',
	'jcool': 'jcool@niuco.com',
	'jay': 'jay@niuco.com'
}

print 'the address of zee is %s' %add['zee']

# then we add a key

add['pop'] = 'pop@niuco.com'
print 'the address of pop is %s' %add['pop']

del add['pop']

print 'now there are %d keys in add.' %len(add)

# ---------this is diffrent with js----------------
for key,value in add.items():
	print 'the address of %s is %s' %( key,value )
if 'jay' in add:
	print 'jay is in add'
