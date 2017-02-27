# this is my shopping list

shoplist = ['spple','mango','carrot','banana']
print 'i have ',len(shoplist),' items to purchase'

for item in shoplist:
	print item
shoplist.append('rice')
print 'now i have ',len(shoplist),' items to purchase'

del shoplist[1]

for item in shoplist:
	print item
shoplist.sort()
print 'now my shoplist is',shoplist
