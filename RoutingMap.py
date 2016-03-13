#!/usr/bin/python2.7
#This Python file uses the following encoding: utf-8
#Author Will CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network
from collections import defaultdict
import fileinput, optparse, string, os, sys, getopt
try:
    import networkx as nx
except ImportError, e:
    import pip
    pip.main(['install', 'networkx'])
    import networkx
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
    with open(cityFile,'r') as cityList:
        for line in cityList:
            if not any(substring in line for substring in "From"):
                if not any(substring in line for substring in '_'):
                    if not line:
                        line = line.replace('-','')
                        info = line.split('   ')[0]
                        info = striplist(info)
                        while '' in info:
                            info.remove('')
                        city = Town(info[0]).lower()
                        print "Found", city
                        city.agacent +=1
                        city2 = Town(info[1]).lower()
                        print "Found", city2
                        milesBetwen = info[2]
                        if city not in cities:
                            cities.append(city)
                        add2graph(city, city2, milesBetween)
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
def userInput(): #getting user input
    myInput = int(1)
    while (myInput != 0):
        myInput = raw_input("What would you like to do:\n1:query directly connected cites: \n2:Look for direct connections: \n3:caclulate the k-hop connection: \n4:Given two query cities print direct connection \n0: Quite\n")
        #myInput = int(myInput)
        if myInput == 1:
            city = raw_input("Please enter the city to query\n").strip().lower()
            if city in Town:
                print (city, " is agacent to ", city.agacent, " Cities")
            else:
                print ("No city found try agian")
        elif myInput == 2:
            print("Not yet Implemented")
        elif myInput == 3:
            print("Not yet Implemented")
        elif myInput == 4:
            print("Not yet Implemented")
        else:
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
