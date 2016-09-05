# Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = raw_input("Enter file:")
fileh = open(name)
counts = dict()
l = list()
hours = list()

for line in fileh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    pieces = line.split(" ")
    l.append(pieces [6])
    
for i in l:
    hours.append(i[:2])

for hour in hours:
        counts [hour] = counts.get(hour , 0) + 1

hours1 = list()
for i,j in counts.items():
	hours1.append((i,j))
    
hours1.sort()
    
for i,j in hours1:
    print i,j