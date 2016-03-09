#/bin/python
#Author Will
#CSCI 305 Programming Lab 2 — Reconstructing Montana’s Road Network
from collections import defaultdict
import fileinput, optparse
class town #object for town
    def adjacency
        self.agacent =0
    def __init__(self,name):
        self.name = name
    def map
        self.roudmap = defaultdict(list)

def add2dict(cityFile):
    str info
    with open(cityFile,'r') as cityList:
        for line in cityList:
            if not line.contains("From") || not line.contains('_'):
                if not line: #building town object
                    info = line.split(' ')[0]
                    info = info.strip()
                    while '' in info
                        info.remove('')
                    town.name = info[0]
                    town.roudmap[town.name] = {info[1],info[2]}
                    town.agacent++

def userInput():
    int myInput = 1
    while (userSelection != 0)
    myInput = input("What would you like to do:\n1:query directly connected cites: \n2:Look for direct connections: \n3:caclulate the k-hop connection: \n4:Given two query cities print direct connection \n0: Quite")
    if myInput == 1:
        city = input("Please enter the city to query")
        if city is in town:
            print city.agacent


    get.chomp

def main(argv):
    cityFile = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:],"f:",["file="])
    except getopt.GetoptError:
        print 'RoutingMap.py -f <file>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'RoutingMap.py -f <file>'
            sys.exit(2)
        elif opt in ('-f', '--file'):
            cityFile = arg
    print "cityFile is ", cityFile
    add2dict(cityFile)
    userInput()

if __name__ == "__main__":
   main(sys.argv[1:])
