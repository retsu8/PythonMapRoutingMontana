#!/usr/bin/python2.7
#This Python file uses the following encoding: utf-8
__author__ = """\n""".join(['Will CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network'])
from collections import defaultdict
import fileinput, optparse, string, os, sys, getopt
try:
    import networkx as nx
except ImportError, e:
    import pip
    pip.main(['install', 'networkx'])
    import networkx as nx
roudmap=nx.Graph()
cities=list()
class Town: #building definition
    def __init__(self,name):
        self.name = name
    agacent = 0

def striplist(l):
    return([x.strip() for x in l])

def parseFile(cityFile):  #building town object dictionary
    print 'adding cities'
    with open(cityFile,'r') as cityList:
        for line in cityList:
            line = line.lower()
            line = line.replace('-----------------------','')
            info = line.split('  ')
            info = striplist(info)
            info = filter(bool, info)
            if len(info) < 3:
                continue
            city = Town(info[0])
            city.agacent = city.agacent + 1
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
    city = Town(city)
    if city in cities:
        print (city, " is agacent to ", city.agacent, " Cities")
    else:
        print ("No city found try agian")
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
            findDirConnected()
        elif myInput == 2:
            print("Not yet Implemented")
        elif myInput == 3:
            print("Not yet Implemented")
        elif myInput == 4:
            print("Not yet Implemented")
        elif myInput == 5:
            map()
        elif myInput not in range(0-5):
            print("Input unreconized please try again")
    print("Goodbye thank you for using the database.")

def main(argv): #main argv for input
    cityFile = ""
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
