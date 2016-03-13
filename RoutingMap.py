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
    def __init__(self, agacent):
        self.agacent = agacent
    def __init__(self,name):
        self.name = name

def striplist(l):
    return([x.strip() for x in l])

def parseFile(cityFile):  #building town object dictionary
    print 'adding cities'
    with open(cityFile,'r') as cityList:
        for line in cityList:
            line = line.lower()
            print 'found', line
            if line.isspace():
                continue
            line = line.replace('-----------------------','')
            info = line.split('  ')
            info = striplist(info)
            while '' in info:
                info.remove('')
            print "adding", info[0]
            city = Town(info[0])
            print "setting agacency", city.agacent
            city.agacent +=1
            if city not in cities:
                cities.append(city)
            add2graph(info[0], info[1], info[-1])
def add2graph(city1, city2, miles):
    if city1 not in roudmap:
        print "adding", city1
        roudmap.add_node(city1)
    if city2 not in roudmap:
        print "adding", city2
        roudmap.add_node(city2)
    if city in roudmap:
        print "Adding distance", miles
        roudmap.add_edge(city1, city2, weigth=miles)
def findDirConnected():
    city = raw_input("Please enter the city to query\n").strip().lower()
    if city in cities:
        print (city, " is agacent to ", city.agacent, " Cities")
    else:
        print ("No city found try agian")
def userInput(): #getting user input
    myInput = int(1)
    while (myInput != 0):
        myInput = raw_input("What would you like to do:\n1:query directly connected cites: \n2:Look for direct connections: \n3:caclulate the k-hop connection: \n4:Given two query cities print direct connection \n0: Quite\n")
        myInput = int(myInput)
        if myInput == 1:
            findDirConnected()
        elif myInput == 2:
            print("Not yet Implemented")
        elif myInput == 3:
            print("Not yet Implemented")
        elif myInput == 4:
            print("Not yet Implemented")
        elif myInput not in range(0-4):
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
