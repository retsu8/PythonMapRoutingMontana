#!/usr/bin/python2.7
#This Python file uses the following encoding: utf-8
__author__ = """\n""".join(['Will CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network'])
from collections import defaultdict
from collections import deque
import fileinput, string, optparse, os, sys, getopt, re
try:
    import networkx as nx
except ImportError, e:
    try:
        import pip
        pip.main(['install', 'networkx'])
        import networkx as nx
    except ImportError, e:
        print "Cant install networkx please resolve this first"
roudmap=nx.MultiGraph()
cities=[]
bad_chars = """[!@#$ -,)(*&^%<>?/\r\n"|{}=+.]:; """

class Town: #building definition
    def __init__(self,name):
        self.name = name
def mystrip(strg):
    """
    Strips bad characters from a string.
    """
    return strg.translate(string.maketrans("", "", ), bad_chars)

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
                intro = True
        for line in cityList:
            line = line.lower()
            line = line.replace('-----------------------','')
            info = line.split('  ')
            info = striplist(info)
            info = filter(bool, info)
            if len(info) < 3:
                continue
            if info[0] not in cities:
                city1 = Town(info[0])
                cities.append(info[0])
            if info[1] not in cities:
                city2 = Town(info[1])
                cities.append(info[1])
            add2graph(info[0], info[1], info[2])
    print "Done importing cities", cities
def map():
    for n1, n2, attr in roudmap.edges(data=True): # unpacking
        print n1, n2, attr['weight']
def directConnection():
    places = ""
    while places != quit:
        places = raw_input("Please enter the cities to query\n or quit to exit: ").strip().lower()
        places = places.split()
        places = striplist(places)
        places[0]=mystrip(places[0])
        places[1]=mystrip(places[1])
        if len(places) != 2:
            print "Wrong amount of places please try agian"
            return
        else:
            try:
                roudmap.edge[places[0]][places[1]]
                print "Yes", roudmap.edge[places[0]][places[1]]
            except:
                print "No"
    return

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
def quarryAgacent():
    city = raw_input("Please enter the city to query\n").strip().lower()
    if city in cities:
        print city, " is agacent to ", len(roudmap.edges(city)), " Cities"
        return
    print "No city found please try agian"
def checkKhop():
    places = ""
    while places != quit:
        places = raw_input("Please enter the cities to query\n or quit to exit: ").strip().lower()
        places = places.split()
        places = striplist(places)
        places[0]=mystrip(places[0])
        places[1]=mystrip(places[1])
        d = places[2]
        if len(places) != 3:
            print "Wrong amount of entries please try agian"
            return
        else:
            try:
                roudmap.edge[places[0]][places[1]]
                print "Yes, 1", roudmap.edge[places[0]][places[1]]
            except:
                print "No"
    return

def userInput(): #getting user input
    myInput = int(1)
    while (myInput != 0):
        myInput = raw_input("What would you like to do:\n1:query directly connected cites: \n2:Look for direct connections: \n3:caclulate the k-hop connection: \n4:Given two query cities print direct connection \n5:Print the map \n0: Quite\n")
        if myInput == '':
            print("Did not enter anything please try agian")
            myInput = int(1)
            continue
        myInput = int(myInput)
        if myInput == 1:
            quarryAgacent()
        elif myInput == 2:
            directConnection()
        elif myInput == 3:
            checkKhop()
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
