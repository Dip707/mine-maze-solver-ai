#!/usr/bin/env python3
from pysat.solvers import Glucose3

from Agent import *  # See the Agent.py file

from queue import Queue,LifoQueue

#### All your code can go here.
#### You can change the main function as you wish. Run this program to see the output. Also see Agent.py code.
# import agent class
# we have three functions we can use
#  Find current location
#  Perceive current location
#  Take action

    # 21 22 23 24 25
    # 16 17 18 19 20
    # 11 12 13 14 15
    # 6  7  8  9  10
    # 1  2  3  4  5
def classifyCells(x):
    if (x == 1 or x == 5 or x == 21 or x == 25):
        return 1
    if (x%5 == 1 or x%5 == 0 or x < 6 or x > 20):
        return 2
    return 0

def main():
    ag = Agent()
    # print('curLoc',ag.FindCurrentLocation())
    # print('Percept ',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Right')
    # print('Percept ',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Right')
    # print('Percept ',ag.PerceiveCurrentLocation())
    
    # ag.TakeAction('Up')
    # print('Percept ',ag.PerceiveCurrentLocation())
    
    # defining variables
    # so basically we have two states in which a cell can be
    # so we keep them as
    # safe - a 
    # mine - not a
    
    # we also keep a set "safe" which keeps all the vertices which are safe
    # initially this set contains 1,1
    
    # also we need to mark how each cell is represented so we keep the naming scheme as follows
    # 21 22 23 24 25
    # 16 17 18 19 20
    # 11 12 13 14 15
    # 6  7  8  9  10
    # 1  2  3  4  5
       
    # we need to map these variables to matrix coordinates
    
    adjDef = [[],[2,6],[1,3,7],[2,4,8],[3,5,9],[4,10],[1,7,11],[2,6,8,12],[3,7,9,13],[4,8,10,14],[5,9,15],[6,12,16],[7,11,13,17],[8,12,14,18],[9,13,15,19],[10,14,20],[11,17,21],[12,16,18,22],[13,17,19,23],[14,18,20,24],[15,19,25],[16,22],[17,21,23],[18,22,24],[19,23,25],[20,24]]
    
    adjList = []
    for i in range(0,26):
        adjList.append([])
    # print(adjList)
    
    ambiguous = []
    for i in range(0,26):
        ambiguous.append(1)
    ambiguous[1] = 0
    # print(ambiguous)
    
    KB = Glucose3()
    KB.add_clause([1])
    
    queueSafe = Queue(maxsize = 50) 
    queueSafe.put(1)
    lastLocation = 1
    while (not queueSafe.empty()):
        # print(adjList,"73")
        currLocation = queueSafe.get()
        ambiguous[currLocation] = 0
        
        # travelBFS(nextLocation)
        queueBFS = Queue(maxsize = 26)
        parent = [-1] * 26
        parent[lastLocation] = lastLocation
        queueBFS.put(lastLocation)
        while not queueBFS.empty():
            x = queueBFS.get()
            if (x == currLocation):
                break
            for y in adjList[x]:
                if (parent[y] == -1):
                    parent[y] = x
                    queueBFS.put(y)
        
        # print(parent)
        
        # backtrack to find the path
        var = currLocation
        stack = LifoQueue(maxsize = 26)
        while (parent[var] != var):
            stack.put(var)
            var = parent[var]
        stack.put(var)
        lastL = lastLocation
        while not stack.empty():
            x,y = ag.FindCurrentLocation()
            assert lastL == (y-1)*5 + x
            curr = stack.get()
            if(lastL != curr):
                if curr == lastL + 1:
                    ag.TakeAction('Right')
                elif curr == lastL - 1:
                    ag.TakeAction('Left')
                elif curr == lastL + 5:
                    ag.TakeAction('Up')
                elif curr == lastL - 5:
                    ag.TakeAction('Down')
                else:
                    # print(curr,lastL)
                    assert False
                lastL = curr
        xx,yy = ag.FindCurrentLocation()
        # assert ag._isAlive == True
        # assert (yy-1)*5 + xx == currLocation
        
        percept = ag.PerceiveCurrentLocation()
        
        if classifyCells(currLocation) == 1:
            a = currLocation
            b = currLocation
            if currLocation == 1:
                a = 2 
                b = 6
            if currLocation == 5:
                a = 4
                b = 10
            if currLocation == 21:
                a = 22
                b = 16
            if currLocation == 25:
                a = 24
                b = 20
            if percept == 0:
                KB.add_clause([a])
                KB.add_clause([b])
            if percept == 1:
                KB.add_clause([-a,-b])
                KB.add_clause([a,b])
            if percept == 2:
                KB.add_clause([-a])
                KB.add_clause([-b]) 
        elif classifyCells(currLocation) == 2:
            a = currLocation
            b = currLocation
            c = currLocation
            if currLocation < 6:
                a = currLocation + 1
                b = currLocation - 1
                c = currLocation + 5
            elif currLocation > 20:
                a = currLocation + 1
                b = currLocation - 1
                c = currLocation - 5
            elif currLocation%5 == 1:
                a = currLocation + 1
                b = currLocation + 5
                c = currLocation - 5
            elif currLocation%5 == 0:
                a = currLocation - 1
                b = currLocation + 5
                c = currLocation - 5
            if percept == 0:
                KB.add_clause([a])
                KB.add_clause([b])
                KB.add_clause([c])
            if percept == 1:
                KB.add_clause([-a,-b,-c])
                KB.add_clause([a,b])
                KB.add_clause([c,b])
                KB.add_clause([a,c])
            if percept == 2:
                KB.add_clause([a,b,c])
                KB.add_clause([-a,-b])
                KB.add_clause([-c,-b])
                KB.add_clause([-a,-c])
            if percept == 3:
                KB.add_clause([-a])
                KB.add_clause([-b])
                KB.add_clause([-c])
        else:
            a = currLocation - 1
            b = currLocation + 1
            c = currLocation + 5
            d = currLocation - 5
            if a == parent[currLocation]:
                a,d = d,a
            elif b == parent[currLocation]:
                b,d = d,b
            elif c == parent[currLocation]:
                c,d = d,c
            if percept == 0:
                KB.add_clause([a])
                KB.add_clause([b])
                KB.add_clause([c])
            if percept == 1:
                KB.add_clause([-a,-b,-c])
                KB.add_clause([a,b])
                KB.add_clause([c,b])
                KB.add_clause([a,c])
            if percept == 2:
                KB.add_clause([a,b,c])
                KB.add_clause([-a,-b])
                KB.add_clause([-c,-b])
                KB.add_clause([-a,-c])
            if percept == 3:
                KB.add_clause([-a])
                KB.add_clause([-b])
                KB.add_clause([-c])
        
        for i in range(1,26):
            if ambiguous[i]:
                if not KB.solve(assumptions=[-i]):
                    for j in adjDef[i]:
                        if ambiguous[j] == 0:
                            adjList[i].append(j)
                            adjList[j].append(i)
                    queueSafe.put(i)
                    ambiguous[i] = 0
                    print(i)
                if not KB.solve(assumptions=[i]):
                    ambiguous[i] = -1
        
        lastLocation = currLocation
    f = False
    for i in range(6,21):
        if(i%5 == 1 or i%5 == 0):
            continue
        if(ambiguous[i-1] == -1 and ambiguous[i+1] == -1 and ambiguous[i+5] == -1 and ambiguous[i-5] == -1):
            print("Gold Infered at location",i%5,i//5  + 1)
            f = True
    
    if not f:
        print("Could not infer gold")     
            
    
                

if __name__=='__main__':
    main()