# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:16:43 2023

@author: Fernando Lasso
"""
import pyamaze
from pyamaze import maze 
from pyamaze import agent
from queue import PriorityQueue

m = maze(10,10)
m.CreateMaze()

xinit = m.rows #swtiching x and y values !!
yinit = m.cols
beginposition = (m.rows, m.cols)
robtot = {}
gtotal = {}
for eachvalue in m.grid:
    gtotal[eachvalue] = 89898989
gtotal[beginposition] = 0 
ftotal = {}
for eachvalue1 in m.grid:
    ftotal[eachvalue1] = 89898989 
htotalinitial = abs(xinit-1) + abs(yinit-1) #goal position is (1,1)   
ftotal[beginposition] = htotalinitial + gtotal[beginposition]
priototal = PriorityQueue() 
priototal.put(((htotalinitial+0),htotalinitial,beginposition))

while not priototal.empty():
    postot = priototal.get()[2]
    #print ('current pos:', postot)
    if postot == (1,1):
        break
    
    for direction in 'NSEW':
        if m.maze_map[postot][direction] == True: #with
            if direction == 'N':
                posfinal = (postot[0]-1, postot[1])
            if direction == 'S':
                posfinal = (postot[0]+1, postot[1])
            if direction == 'E':
                posfinal = (postot[0], postot[1]+1)
            if direction == 'W':
                posfinal = (postot[0], postot[1]-1)

            posfinaltotal = list(posfinal)           
            htotalnew = abs(posfinaltotal[0] - 1) + abs(posfinaltotal[1] - 1)
            newgtotal = gtotal[postot] + 1
            #print ('newgtotal:', newgtotal)
            newftotal = newgtotal + htotalnew
            #print ('newftotal:', newftotal)
                    
            if newftotal < ftotal[posfinal]:
                gtotal[posfinal] = newgtotal
                ftotal[posfinal] = newftotal
                priototal.put((newftotal, htotalnew, posfinal))
                robtot[posfinal] = postot
                #print ('robot movement:', robtot)

robfinal = {}
goalcell = (1,1)
while goalcell != beginposition:
    robfinal[robtot[goalcell]] = goalcell
    goalcell = robtot[goalcell]
#print ('robot final:', robfinal)

robot = agent(m)
mainplayer = agent(m, color='red', shape='arrow')
m.tracePath({robot:robfinal})
m.enableArrowKey(mainplayer)

m.run()






