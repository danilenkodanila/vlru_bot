import re
import sys
import pars


listId = []
listId.append(0)


listUsers = []

f = open('users.txt')
for line in f:
	listUsers.append(line.replace("\n",""))


print(listUsers)