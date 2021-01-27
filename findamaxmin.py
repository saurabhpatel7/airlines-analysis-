import csv
import sys
import operator

if len(sys.argv) < 2:
    message = bcolors.BOLD + "Usage: python findmax.py <input file>" + bcolors.ENDC
    sys.exit(message)

# Take the input file
input_file = sys.argv[1]

# dictionaries
origin = {}
dest = {}
carrier = {}

inp = open(input_file,"rb")

first=0
# loop over file
for line in inp:
	
	#ignore first
	if first==0:
		first=1
		continue

	arr = line.split(",")

	car = arr[8]
	ori = arr[16]
	des = arr[17]

	if car in carrier:
		carrier[car]+=1
	else:
		carrier[car]=0

	if ori in origin:
		origin[ori]+=1
	else:
		origin[ori]=0

	if des in dest:
		dest[des]+=1
	else:
		dest[des]=0

# Sort the inputs
carrier = sorted(carrier.items(), key=operator.itemgetter(1),reverse=True)
dest = sorted(dest.items(), key=operator.itemgetter(1),reverse=True)
origin = sorted(origin.items(), key=operator.itemgetter(1),reverse=True)

# print maximums
print [x[0] for x  in (carrier[0:20])]
print [x[0] for x  in (origin[0:20])]
print [x[0] for x  in (dest[0:20])]