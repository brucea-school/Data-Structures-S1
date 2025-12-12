import numpy
import numpy as np
f = open("challengeOnly.txt", "r")
g = f.readlines()
teamsd = {}
for i in g:
    g[g.index(i)] = i[:len(i)-1]

for i in g:
    for j in g[g.index(i)].split():
        teamsd[j] = 0

print(teamsd)
match = 0

for i in g:
    match += 1
    print("*** match "+str(match)+" ***")
    print("Red Alliance:  "+str(i.split()[0])+" "+str(i.split()[1])+" "+str(i.split()[2]))
    print("Blue Alliance: " + str(i.split()[3]) + " " + str(i.split()[4]) + " " + str(i.split()[5]))
    intake = input("Enter the red team's ranking points: ")
    while int(intake)>4 or int(intake)<0:
        print("Ranking points should be between 0 and 4:")
        intake = input("Enter the red team's ranking points: ")
    teamsd[str(i.split()[0])] += int(intake)
    teamsd[str(i.split()[1])] += int(intake)
    teamsd[str(i.split()[2])] += int(intake)

    intake = input("Enter the blue team's ranking points: ")
    while int(intake) > 4 or int(intake) < 0:
        print("Ranking points should be between 0 and 4:")
        intake = input("Enter the blue team's ranking points: ")
    teamsd[str(i.split()[3])] += int(intake)
    teamsd[str(i.split()[4])] += int(intake)
    teamsd[str(i.split()[5])] += int(intake)


#teamsd is total value not avrage