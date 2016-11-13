# -*- coding: utf-8 -*-

listUsers = []

f = open('users.txt')
for line in f:
	listUsers.append(line.replace("\n",""))


print(listUsers)