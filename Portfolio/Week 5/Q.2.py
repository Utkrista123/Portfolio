'''Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument).'''

import sys
value = sys.argv[0: ]
print(f"There are {len(value)} number of arguments.")
