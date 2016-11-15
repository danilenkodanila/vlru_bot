import re
import sys
import pars

listUsers = []
f = open('users.txt', 'r')
for line in f:
		listUsers.append(line.replace("\n",""))
f.close()

print('listUsers при запуске', listUsers)

def addUser(user):
	global listUsers
	listUsers.append(user)
	f = open('users.txt', 'a')
	f.write(str(user) + '\n')
	f.close()
	listUsers = []
	f = open('users.txt', 'r')
	for line in f:
		listUsers.append(line.replace("\n",""))
	print('listUsers sendSpam addUser', listUsers)
	f.close()
	return listUsers

def deleteUser():
	global listUsers
	f = open('users.txt', 'w')
	for element in listUsers:
		f.write(str(element) + '\n')
	f.close()
	print('listUsers sendSpam deleteUser', listUsers)
	return listUsers
