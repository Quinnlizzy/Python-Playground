#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends)
print(friends_tuple)
print(friends_set)


# ›['John', 'Michael', 'Terry', 'Eric', 'Graham']
# ›('John', 'Michael', 'Terry', 'Eric', 'Graham')
# ›{'John', 'Michael', 'Terry', 'Eric', 'Graham'}




#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set))

#{'Eric', 'Graham'}


