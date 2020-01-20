# -*- coding: utf-8 -*-
"""
Altered on: 1/15/2020

@author: lachlan Sinclair
"""

import Dominion
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla","*Lachlan"]

#number of curses and victory cards
#nV = testUtility.getnV(player_names)
nV = testUtility.buggedGetnV(player_names)
nC = -10 + 10 * len(player_names)

#call MakeBoxes
box = testUtility.makeBoxes(nV)

#set the supply order
supply_order = testUtility.getSupplyOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.pickTen(box)

#The supply always has these cards
supply = testUtility.addBaseSupply(supply, nV, nC, player_names)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.createPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)