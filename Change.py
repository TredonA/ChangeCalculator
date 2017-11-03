from math import *
print "Hi! Welcome to Tre's change calculator."

changeNeeded = input("Please enter the amount of change the customer needs back in XX.XX format: ")
floatChangeNeeded = float(changeNeeded)
assert floatChangeNeeded >= 0
cashChange = floor(floatChangeNeeded)
floatChangeNeeded -= cashChange
centsNeeded = floatChangeNeeded * 100
assert centsNeeded >= 0 and centsNeeded < 100

# Initialize four distinct variables to hold the number of Quarters, Dimes,
# Nickels, and Pennies needed respectively.

numQuartersNeeded = 0
numDimesNeeded = 0
numNickelsNeeded = 0
numPenniesNeeded = 0

# For Quarters, Dimes, and Nickels, calculate how many times the respective
# currencies divide the remaining amount of change. Afterwards, subtract the
# amount of respective coins needed from the remaining amount of change.

numQuartersNeeded += centsNeeded // 25
int(numQuartersNeeded)
centsNeeded -= numQuartersNeeded * 25

numDimesNeeded += centsNeeded // 10
int(numDimesNeeded)
centsNeeded -= numDimesNeeded * 10

numNickelsNeeded += centsNeeded // 5
int(numNickelsNeeded)
centsNeeded -= numNickelsNeeded * 5

# For pennies, dividing the remaining amount of change by 1 is completely
# unnecessary. Whatever remaining change is needed after taking into account
# coins of a higher currency value can be returned with pennies
numPenniesNeeded += centsNeeded
int(numPenniesNeeded)

print "You will need to give the customer " + str(numQuartersNeeded)
print "quarter(s), " + str(numDimesNeeded) + " dime(s), "
print str(numNickelsNeeded) + " nickel(s), and " + str(numPenniesNeeded) + "penny (ies)."
