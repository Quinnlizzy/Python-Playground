
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

#['Exercise: fill me with names']

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(','.join(csv.split(';')))
print(','.join(csv.split(';')).split(':'))
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

#›Eric,John,Michael,Terry,Graham:TerryG,Brian
#›['Eric,John,Michael,Terry,Graham', 'TerryG,Brian']
#›['Exercise: fill me with names']



csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(','.join(csv.split(';')))
print(','.join(csv.split(';')).split(':'))
print(','.join(','.join(csv.split(';')).split(':')))
friends_list = ['Exercise: fill me with names']
print(friends_list)

# ›Eric,John,Michael,Terry,Graham:TerryG,Brian
# ›['Eric,John,Michael,Terry,Graham', 'TerryG,Brian']
# ›Eric,John,Michael,Terry,Graham,TerryG,Brian
# ›['Exercise: fill me with names']



csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print((','.join(','.join(csv.split(';')).split(':'))).split(','))
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

# ›['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']
# ›['Exercise: fill me with names']



csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)

#›['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']