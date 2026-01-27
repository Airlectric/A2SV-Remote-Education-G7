import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

phonebook = {}

for _ in range(n):
    name, value = input().split()
    phonebook[name] = value

for line in sys.stdin:
    key = line.strip()
    
    if key in phonebook:
        print(f"{key}={phonebook[key]}")
    else:
        print("Not found")
