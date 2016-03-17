#!/usr/bin/python2.7
#This Python file uses the following encoding: utf-8
__author__ = """\n""".join(['Will CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network'])
from collections import defaultdict, deque
import fileinput, string, optparse, os, sys, getopt, re
try: #checking to make sure networkx is installed
    import networkx as nx
except ImportError, e:
    try: #if not installed install it
        import pip
        pip.main(['install', 'networkx'])
        import networkx as nx
    except ImportError, e:
        print "Cant install networkx please resolve this first"
roudmap=nx.MultiGraph() #setting up graph for MultiGraph
cities=[] #list of cities for k-hop route
bad_chars = """[!@#$ -,)(*&^%<>?/\r\n"|{}=+.]:; """ #list of char to remove from city names

class Town: #building city object for Town
    def __init__(self,name):
        self.name = name
def mystrip(strg): #strip &bad_char from string
    """
    Strips bad characters from a string.
    """
    return strg.translate(string.maketrans("", "", ), bad_chars)

'''
def breadth_first_search(source, destination): #breadth_first_search algorithm for finding path to nodes
     print "Finding fewest hops to ", destination, "from", source
     path = list()
     path = path.append(source)
     neighbors = nx.neighbors(roudmap, source)
     def recursion(source, destination, path, neighbors): #recursion piece for search
         if destination not in neighbors:
            for place in neighbors:
                if place == destination:
                    return path.append(place)
                if place in path:
                    continue
                else:
                    recursion(place, destination, path nx.neighbors(roudmap,source))
     recursion(source, destination, path, neighbors)
     return path
'''

def striplist(l): #remove white space from list
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
    print len(cities) #debugging
    city = raw_input("Please enter the city to query\n").strip().lower()
    for place in roudmap.nodes():
        if city == place:
            print "%s is adjacent to %s cities" % (city, len(roudmap.edges(place)))
            #print (city + " is adjacent to " + len(roudmap.edges(place)) + " cities")
            return
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
            directConnection()
        elif myInput == 3:
            checkKhop()
        elif myInput == 4:
            checkConnection()
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

if __name__ == "__main__": #send python to main loop to start
   main(sys.argv[1:])
