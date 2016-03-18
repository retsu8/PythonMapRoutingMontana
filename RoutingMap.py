#!/usr/bin/python2.7
#This Python file uses the following encoding: utf-8
<<<<<<< HEAD
__author__ = """\n""".join(['Will CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network'])
from collections import defaultdict, deque
import fileinput, string, optparse, os, sys, getopt, re
try: #checking to make sure networkx is installed
=======
__author__ = """\n""".join(['William Paddock and Ryan Darnell CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network'])
from collections import defaultdict
from collections import deque
import fileinput, optparse, string, os, sys, getopt
try:
>>>>>>> refs/remotes/origin/Ryan
    import networkx as nx
except ImportError, e:
    try: #if not installed install it
        import pip
        pip.main(['install', 'networkx'])
        import networkx as nx
    except ImportError, e:
        print "Cant install networkx please resolve this first"
<<<<<<< HEAD
roudmap=nx.MultiGraph() #setting up graph for MultiGraph
cities=[] #list of cities for k-hop route
bad_chars = """[!@#$-,)(*&^%<>?/\r\n"|{}=+.]:;""" #list of char to remove from city names

class Town: #building city object for Town
    def __init__(self,name):
        self.name = name
def mystrip(strg): #strip &bad_char from string
    """
    Strips bad characters from a string.
    """
    return strg.translate(string.maketrans("", "", ), bad_chars)

def striplist(l): #remove white space from list
=======
roudmap=nx.Graph()
cities=list()

def striplist(l):
>>>>>>> refs/remotes/origin/Ryan
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
<<<<<<< HEAD

            add2graph(info[0], info[1], int(info[2]))
    print "Done importing cities", cities
def map(): #print map of graph
    for n1, n2, attr in roudmap.edges(data=True): # unpacking
        print n1, n2, attr['weight']
def directConnection(): #find if town a is directly connected to town b
    places = ""
    while places != quit:
        places = raw_input("Please enter the cities to query, split with comma\n or quit to exit: ").strip().lower()
        places = places.split(",")
        places = striplist(places)
        if len(places) != 2:
            print "Wrong amount of entries please try agian, did you forget the comma?"
            return
        else:
            places[0]=mystrip(places[0])
            places[1]=mystrip(places[1])
            try:
                roudmap.edge[places[0]][places[1]]
                print "Yes", roudmap.edge[places[0]][places[1]]
            except:
                print "No"
    return

def add2graph(city1, city2, miles): #add lots of stuff to graph, building graph
=======
            
            add2graph(info[0], info[1], info[2])
    print "Done importing cities\n"
    
def map():
    for n1, n2, attr in roudmap.edges(data=True): # unpacking
        print n1, n2, attr['weight']
        
def add2graph(city1, city2, miles):
>>>>>>> refs/remotes/origin/Ryan
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
            return
<<<<<<< HEAD
    for place in cities: # unpacking
        if city == place.name:
            print (city, " is agacent to ", place.agacent, " cities")
            return
    print "No city found please try agian"

def checkKhop(): #c if possible to reace destination from starting point within d times
    places = ""
    while places != quit:
        places = raw_input("Please enter the cities to query and the number of hops space with commas\n or quit to exit: ").strip().lower()
        places = places.split(',')
        places = striplist(places)
        if len(places) != 3:
            print "Wrong amount of entries please try agian, did you forget the comma?"
            return
        else:
            places[0]=mystrip(places[0])
            places[1]=mystrip(places[1])
            d = places[2]
            try:
                roudmap.edge[places[0]][places[1]]
                print roudmap.edge[places[0]][places[1]]
            except:
                distance = 0
                place_old = None
                path = nx.shortest_path(roudmap,source=places[0],target=places[1], weight=d)
                for place in path:
                    if place_old == None:
                        place_old = place
                    print roudmap.edge[place_old][place]['weight']
                    distance = distance + roudmap.edge[place_old][place]['weight']
                    place_old = place
                if len(path) > d:
                    print "Not possible in ", d, "hops\n0"
                print "The shortest path is", path, "at ", len(path), "hops.\nThe distence is", distance
    return

def checkConnection():
    places = ""
    while places != quit:
        places = raw_input("Please enter the cities to query, split with comma\n or quit to exit: ").strip().lower()
        places = places.split(",")
        places = striplist(places)
        if len(places) != 2:
            print "Wrong amount of entries please try agian, did you forget the comma?"
            return
        else:
            places[0]=mystrip(places[0])
            places[1]=mystrip(places[1])
            try:
                roudmap.edge[places[0]][places[1]]
                print roudmap.edge[places[0]][places[1]]
            except:
                place_old = None
                path = nx.bidirectional_dijkstra(roudmap,source=places[0],target=places[1])
                print "The shortest path is", path
    return

=======
    print "No city found!\n"

def isDirectConnection(city1, city2):
    if roudmap.has_edge(city1, city2):
        print "%s is directly connected to %s" % (city1, city2)
    else:
        print "No connection found between %s and %s" % (city1, city2)

def kHopping(origin, targetCity, totalK):
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
        #neighbor list is depleted. jump up a neighbor
        else:
            network.pop()
            lastCity = path.pop()
            if len(network)!=0:
                currentCity = network[len(network)-1][0] 
                currentK = currentK - int(roudmap.get_edge_data(lastCity, currentCity)["weight"])
                continue
            else: #list empty, so break
                foundPath = False
                break
        path.append(currentCity)
        currentK = currentK + int(roudmap.get_edge_data(lastCity,currentCity)["weight"])

            
        if currentCity == targetCity:
            if currentK <= totalK:
                
                pathway = origin
                path.pop(0)
                for city in path:
                    pathway = pathway + " --> " + city

                print ("\nThe pathway from %s to %s within %s miles is:") % (origin, targetCity, totalK)
                print pathway + "\n"
                path = [];
                foundPath = True
                break
            else:
                currentK = currentK - int(roudmap.get_edge_data(lastCity, currentCity)["weight"])
                path.pop()
                currentCity = network[len(network)-1][0] 
                continue
        elif currentK > totalK:
            currentK = currentK - int(roudmap.get_edge_data(lastCity, currentCity)["weight"])
            path.pop()
            currentCity = network[len(network)-1][0] 
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
            network.append(neighbors)

    if not foundPath:
        print ("\nNo path found from %s to %s in %s within miles") % (origin, targetCity, totalK)

def isConnected(origin, targetCity):
    path = [origin]
    network = []
    foundPath = False
    lastCity = origin
    currentCity = origin

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
        #neighbor list is depleted. jump up a neighbor
        else:
            network.pop()
            lastCity = path.pop()
            if len(network)!=0:
                currentCity = network[len(network)-1][0] 
                continue
            else: #list empty, so break
                foundPath = False
                break
        path.append(currentCity)
            
        if currentCity == targetCity:
            pathway = origin
            path.pop(0)
            for city in path:
                pathway = pathway + " --> " + city
            print ("\nYES: One pathway from %s to %s is:") % (origin, targetCity)
            print pathway + "\n"
            path = [];
            foundPath = True
            break

        elif roudmap.has_edge(currentCity, targetCity):
            neighbors = [currentCity, targetCity]
            network.append(neighbors)
            
        else:
            if len(network) < 4:
                neighbors = []
                #keep track of city that was branched
                neighbors.append(currentCity)
                for neighborino in roudmap.neighbors(currentCity):
                    if neighborino != lastCity and neighborino != currentCity:
                        neighbors.append(neighborino)
                network.append(neighbors)

    if not foundPath:
        print ("\nNO: No path found from %s to %s in %s within miles") % (origin, targetCity, totalK)

    
>>>>>>> refs/remotes/origin/Ryan
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
        if myInput == '' or not is_number(myInput):
            print("Invalid input... please try again.")
            myInput = int(1)
            continue
        myInput = int(myInput)
        if myInput == 0:
            continue
        elif myInput == 1:
            findDirConnected()
        elif myInput == 2:
<<<<<<< HEAD
            directConnection()
        elif myInput == 3:
            checkKhop()
        elif myInput == 4:
            checkConnection()
=======
            city1 = raw_input("List the first city:  ")
            city2 = raw_input("List the second city: ")
            if roudmap.has_node(city1) and roudmap.has_node(city2):
                isDirectConnection(city1.lower(), city2.lower())
            else:
                print "Sorry, one or more cities does not exist. Please try again\n"
                continue
        elif myInput == 3:
            city = raw_input("List the first city:  ")
            target = raw_input("List the second city: ")
            if roudmap.has_node(city) and roudmap.has_node(target):
                k_hop = raw_input("Set the max distance: ")
                kHopping(city.lower(), target.lower(), int(k_hop))
            else:
                print "Sorry, one or more cities does not exist. Please try again\n"
                continue
        elif myInput == 4:
            city = raw_input("List the first city:  ")
            target = raw_input("List the second city: ")
            if roudmap.has_node(city) and roudmap.has_node(target):
                kHopping(city.lower(), target.lower(), int(k_hop))
            else:
                print "Sorry, one or more cities does not exist. Please try again\n"
                continue
            isConnected(city.lower(), target.lower())
>>>>>>> refs/remotes/origin/Ryan
        elif myInput == 5:
            map()
        elif myInput not in range(0-5):
            print("Input unreconized please try again")
    print("Goodbye thank you for using the database.")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

    
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

if __name__ == "__main__": #send python to main loop to start
   main(sys.argv[1:])
