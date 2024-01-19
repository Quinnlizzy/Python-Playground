friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)

# ›['John', 'Michael', 'Terry', 'Eric', 'Graham']
# ›['Eric', 'Graham', 'John', 'Michael', 'Terry']
# ›['Terry', 'Michael', 'John', 'Graham', 'Eric']
# ›['Eric', 'Graham', 'John', 'Michael', 'Terry']

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
cars.sort()
print(cars)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)

# ›['John', 'Michael', 'Terry', 'Eric', 'Graham']
# ›[130, 308, 328, 535, 740, 911]
# ›['Terry', 'Michael', 'John', 'Graham', 'Eric']
# ›['Eric', 'Graham', 'John', 'Michael', 'Terry']

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
print(sum(cars))

# ›['John', 'Michael', 'Terry', 'Eric', 'Graham']
# ›2952

friends = ['John','Michael','Terry','Eric','Graham']
print(friends)
print(max(friends))

# ›['John', 'Michael', 'Terry', 'Eric', 'Graham']
# ›Terry

friends.append('TerryG')
# ['John', 'Michael', 'Terry', 'Eric', 'Graham', 'TerryG']

friends.insert(1,'TerryG')
#['John', 'TerryG', 'Michael', 'Terry', 'Eric', 'Graham']

friends.remove('Terry')
#['John', 'Michael', 'Eric', 'Graham']

friends.pop()
#pops out last one in list and stores to memory for potential use later
#['John', 'Michael', 'Terry', 'Eric']
#can select which one you want to pop by putting a number in the brackets

friends.clear()
#empties the list altogether but the empty list remains
del friends
#deletes the list itself as a container
del friends[2]
#would just delete the third friend - the list would remain


#copying lists
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
del friends[2]
new_friends = friends[:]
print(friends)
print(new_friends)

# ›['John', 'Michael', 'Eric', 'Graham']
# ›['John', 'Michael', 'Eric', 'Graham']

new_friends = friends.copy()
#does the same thing as the above

new_friends = list(friends)
#again, does the same thing as the above
