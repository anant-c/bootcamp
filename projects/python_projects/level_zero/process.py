import sys

for line in sys.stdin:

    stripped_line = line.strip()

    uppercased_line = stripped_line.upper()

    print(uppercased_line)