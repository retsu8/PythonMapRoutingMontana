#!/usr/bin/python2.7
#This Python file uses the following encoding: utf-8
__author__ = """\n""".join(['William Paddock and Ryan Darnell CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network'])
from collections import defaultdict
from collections import deque
import fileinput, optparse, string, os, sys, getopt
try:
    import networkx as nx
except ImportError, e:
    try:
        import pip
        pip.main(['install', 'networkx'])
        import networkx as nx
    except ImportError, e:
        print "Cant install networkx please resolve this first"
roudmap=nx.Graph()
cities=list()
#global path
class Town: #building definition
    def __init__(self,name):
        self.name = name
    agacent = 0

def breadth_first_search(g, source):
     queue = deque([(None, source)])
     enqueued = set([source])
     while queue:
         parent, n = queue.popleft()
         yield parent, n
         new = set(g[n]) - enqueued
         enqueued |= new
         queue.extend([(n, child) for child in new])

def striplist(l):
    return([x.strip() for x in l])

def parseFile(cityFile):  #building town object dictionary
    print 'adding cities'
    with open(cityFile) as cityList:
        intro = False
        while (not intro):
            line = cityList.readline()
            line = line.lower()
            if "from" in line:
                cityList.readline()
                intro = True
        for line in cityList:
            line = line.lower()
            line = line.replace('-----------------------','')
            info = line.split('  ')
            info = striplist(info)
            info = filter(bool, info)
            
            
            if len(info) < 3:
                continue
            
            add2graph(info[0], info[1], info[2])
    print "Done importing cities"
def map():
    for n1, n2, attr in roudmap.edges(data=True): # unpacking
        print n1, n2, attr['weight']
def add2graph(city1, city2, miles):
    if city1 not in roudmap:
        #print "adding", city1
        roudmap.add_node(city1)
    if city2 not in roudmap:
        #print "adding", city2
        roudmap.add_node(city2)
    if city1 in roudmap:
        #print "Adding distance", miles
        roudmap.add_edge(city1, city2, weight=miles)
def findDirConnected():
    
    city = raw_input("Please enter the city to query\n").strip().lower()
    for place in roudmap.nodes():
        if city == place:
            print "%s is adjacent to %s cities" % (city, len(roudmap.edges(place)))
            #print (city + " is adjacent to " + len(roudmap.edges(place)) + " cities")
            return
    print "No city found!\n"

def isDirectConnection(city1, city2):
    if roudmap.has_edge(city1, city2):
        print "%s is directly connected to %s" % (city1, city2)
    else:
        print "No connection found between %s and %s" % (city1, city2)



def kHopping(city1, target, currentK, totalK, path):
    path.append(city1)
    if city1 == target:
        print ("if1 taken with %s as current") % city1
        if currentK <= totalK:
            print ("The following path will take you to %s from %s\n") % (target, path[0])
            for city in path:
                print (" %s -->") % city

            path = [];
            return True
        else:
            print ("No path was found within the specified distance")
            return False
    elif (currentK > totalK):
        print ("No path was found within the specified distance")
        return False
    elif roudmap.has_edge(city1, target):
        return kHopping(target, target, (currentK + int(roudmap.get_edge_data(city1,target)["weight"])), totalK, path)
    else:
        for current in roudmap.neighbors(city1):
            if kHopping(current, target, (currentK + int(roudmap.get_edge_data(city1,current)["weight"])), totalK, path):
                return True

def kHoppingWhilst(origin, targetCity, totalK):
    path = [origin]
    network = []
    foundPath = False
    lastCity = origin
    currentCity = origin
    currentK = 0

    #Build starting network
    neighbors = []
    neighbors.append(origin)
    for neighborino in roudmap.neighbors(origin):
        if neighborino != lastCity and neighborino != currentCity:
            neighbors.append(neighborino)
    network.append(neighbors)
    
    while len(network) > 0:
        #update currentCity
        lastCity = network[len(network)-1][0]
        #grab next element from the neighbor list
        if len(network[len(network)-1]) > 1:
            currentCity = network[len(network)-1].pop()
            #print ("Current: %s") % currentCity
            #print ("Last: %s\n") % lastCity
        #neighbor list is depleted. jump up a neighbor
        else:
            network.pop()
            lastCity = path.pop()
            if len(network)!=0:
                #lastCity = currentCity
                currentCity = network[len(network)-1][0] #path[len(path)-1]
                currentK = currentK - int(roudmap.get_edge_data(lastCity, currentCity)["weight"])
                continue
            else: #list empty, so break
                print "No path found"
                foundPath = False
                break
            print ("Current: %s") % currentCity
            print ("Last: %s\n") % lastCity
        path.append(currentCity)
        currentK = currentK + int(roudmap.get_edge_data(lastCity,currentCity)["weight"])

            
        if currentCity == targetCity:
            if currentK <= totalK:
                print ("The following path will take you to %s from %s\n") % (targetCity, origin)
                for city in path:
                    print (" %s -->") % city
                path = [];
                foundPath = True
                break
            else:
                print ("%s to %s in length: %s") % (lastCity, targetCity, currentK)
                print path
                currentK = currentK - int(roudmap.get_edge_data(lastCity, currentCity)["weight"])
                path.pop()
                
                #print("Close but too large")
                currentCity = network[len(network)-1][0] #path[len(path)-1]
                continue
        elif currentK > totalK:
            currentK = currentK - int(roudmap.get_edge_data(lastCity, currentCity)["weight"])
            path.pop()
            #print ("Too Large")
            currentCity = network[len(network)-1][0] #path[len(path)-1]
            continue
        elif roudmap.has_edge(currentCity, targetCity):
            neighbors = [currentCity, targetCity]
            network.append(neighbors)
        else:
            neighbors = []
            #keep track of city that was branched
            neighbors.append(currentCity)
            for neighborino in roudmap.neighbors(currentCity):
                if neighborino != lastCity and neighborino != currentCity:
                    neighbors.append(neighborino)
            #print len(neighbors)
            network.append(neighbors)

    if not foundPath:
        print ("No path found from %s to %s in %s miles") % (origin, targetCity, totalK)
        
    
def userInput(): #getting user input
    myInput = int(1)
    while (myInput != 0):
        myInput = raw_input("What would you like to do:\n" +
                            "1:query directly connected cites: \n" +
                            "2:Look for direct connections: \n" +
                            "3:caclulate the k-hop connection: \n" +
                            "4:Given two query cities print direct connection \n" +
                            "5:Print the map \n" +
                            "0: Quit\n")
        if myInput == '':
            print("Did not enter anything please try agian")
            myInput = int(1)
            continue
        myInput = int(myInput)
        if myInput == 0:
            continue
        elif myInput == 1:
            findDirConnected()
        elif myInput == 2:
            city1 = raw_input("List the first city:  ")
            city2 = raw_input("List the second city: ")
            isDirectConnection(city1.lower(), city2.lower())
        elif myInput == 3:
            city1 = raw_input("List the first city:  ")
            target = raw_input("List the second city: ")
            k_hop = raw_input("Set the max distance: ")
            path = []
            #kHopping(city1.lower(), target.lower(), 0, int(k_hop), path)
            kHoppingWhilst(city1.lower(), target.lower(), int(k_hop))
        elif myInput == 4:
            print("Not yet Implemented")
        elif myInput == 5:
            map()
        elif myInput not in range(0-5):
            print("Input unreconized please try again")
    print("Goodbye thank you for using the database.")

def main(argv): #main argv for input
    cityFile = "city1.txt"
    print "Grabbing files for city Map"
    try:
        opts, args = getopt.getopt(sys.argv[1:],"f:",["file="])
    except getopt.GetoptError:
        print ("RoutingMap.py -f <file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ("RoutingMap.py -f <file>")
            sys.exit(2)
        elif opt in ('-f', '--file'):
            cityFile = arg
    print ("City list is ", cityFile)
    parseFile(cityFile)
    userInput()

if __name__ == "__main__":
   main(sys.argv[1:])
