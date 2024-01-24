msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(list(msg))

# ›['W', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '1', '0', '1', ':', ' ', 'S', 'p', 'l', 'i', 't', ' ', 'a', 'n', 'd', ' ', 'J', 'o', 'i', 'n']





msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())

#['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']




msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())
print(msg.split(' '))

#['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
#['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']





msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())
print(msg.split(' '), type(msg.split(' ')))

#['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
#['Welcome', '', 'to', '', 'Python', '', '101:', 'Split', '', 'and', 'Join'] <class 'list'>





msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(csv.split(','))

#['Eric', 'John', 'Michael', 'Terry', 'Graham']





msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print('-'.join(friends_list))

#Eric-John-Michael-Terry-Graham



msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(''.join(friends_list))

#EricJohnMichaelTerryGraham



msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(''.join(friends_list))

print(''.join(msg.split()))

#EricJohnMichaelTerryGraham
#WelcometoPython101:SplitandJoin



msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(''.join(friends_list))

print(''.join(msg.split()))
print(msg.replace(' ', ''))

#EricJohnMichaelTerryGraham
#WelcometoPython101:SplitandJoin
#WelcometoPython101:SplitandJoin