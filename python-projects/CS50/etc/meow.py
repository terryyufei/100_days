"""
import sys

if len(sys.argv) == 1:
    print ("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")   
else:
    print("Usage: meow.py")
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-n", default=1, type=int )
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
