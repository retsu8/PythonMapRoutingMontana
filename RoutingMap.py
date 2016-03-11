#!/usr/bin/python2.7
#This Python file uses the following encoding: utf-8
#Author Will CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network
from collections import defaultdict
import netwworkx as nx
import fileinput, optparse, string, os, sys, getopt

roudmap = defaultdict(list)
class Town: #building definition
    def __init__(self, agacent):
        self.agacent = agacent
    def __init__(self,name):
        self.name = name

def striplist(l):
    return([x.strip() for x in l])

def add2dict(cityFile):  #building town object dictionary
    with open(cityFile,'r') as cityList:
        for line in cityList:
            if not any(substring in line for substring in "From"):
                if not any(substring in line for substring in '_'):
                    if not line:
                        info = line.split(' ')[0]
                        info = striplist(info)
                        while '' in info:
                            info.remove('')
                        city = Town(info[0]).lower()
                        roudmap[city.lower()] = {info[1],info[2]}
                        city.agacent +=1
                        #G=nx.Graph()
                        #G.add_node()
                        #G.add_edge()

def userInput(): #getting user input
    myInput = 1
    while (myInput != 0):
        myInput = input("What would you like to do:\n1:query directly connected cites: \n2:Look for direct connections: \n3:caclulate the k-hop connection: \n4:Given two query cities print direct connection \n0: Quite\n")
        myInput = int(myInput)
        if myInput == 1:
            city = input("Please enter the city to query\n").strip().lower()
            if city in roudmap.keys():
                print (city, " is agacent to ", city.agacent, " Cities")
            else:
                print ("No city found try agian")
        elif myInput == 2:
            print("Working on it")
        elif myInput == 3:
            print("Working on it")
        elif myInput == 4:
            print("Working on it")
        else:
            print("Input unreconized please try again")
    print("Goodbye thank you for using the database.")

def main(argv): #main argv for input
    cityFile = ""
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
    add2dict(cityFile)
    userInput()

if __name__ == "__main__":
   main(sys.argv[1:])
