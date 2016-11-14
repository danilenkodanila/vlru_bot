# -*- coding: utf-8 -*-

import threading
import pars

i = 0

def printit():
  s = []
  threading.Timer(3600, printit).start()
  s = pars.update()


printit()

# listUsers = []



# f = open('users.txt')
# for line in f:
# 	listUsers.append(line.replace("\n",""))



# print(listUsers)