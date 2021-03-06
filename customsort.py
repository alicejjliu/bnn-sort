import sys
import argparse
from functools import cmp_to_key

parser = argparse.ArgumentParser(description = "Sort a list of arbitrary strings using a biological neural network connected to a mechanical-electric interface")
parser.add_argument("input", type = str, help = "input file path")
parser.add_argument("-o", "--output", type = str, help = "output file path")
parser.add_argument("-a", "--ascending", action = "store_false")

cmpdict = {}
def compare(a, b):
    if ((a, b) in cmpdict):
        return cmpdict[(a, b)]
    if ((b, a) in cmpdict):
        return -cmpdict[(b, a)]
    user_in = ""
    valid_in = ("1", "2", "3")
    while (user_in not in valid_in):
        user_in = input(("Is " + a + " better than " + b + "? (1 if yes, 2 if no, 3 if they're the same): "))
    if (user_in == "1"):
        cmpdict[(a, b)] = 1
        return 1
    elif (user_in == "2"):
        cmpdict[(a, b)] = -1
        return -1
    elif (user_in == "3"):
        cmpdict[(a, b)] = 0
        return 0
    return 0

args = parser.parse_args()
inlist = []

with open(args.input, "r") as infile:
    for line in infile:
        inlist.append(line.rstrip())
outlist = sorted(inlist, key = cmp_to_key(compare), reverse = args.ascending)

if (args.output is None):
#We output to stdout the sorted list
    for i in outlist:
        print(i)
else:
    with open(args.output, "w") as outfile:
        for i in outlist:
            outfile.write(i + "\n")
