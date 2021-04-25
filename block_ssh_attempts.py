#!/usr/bin/python3

#probeer te zoeken achter een string in dit geval invalid user
search = "Invalid user"

#ik open de file en open deze op read.
file1 = open("sshdlog", "r")
#ik maak van file1 iets gemakkelijker en ik zeg daar ook voor te lezen en de lijnen te splitten zodat het niet verticaal kwam (was bij mij een voorval)
readfile = file1.read().split('/n')
#ik zoek achter invalid user in mijn file (dit is nog niet volledig, ik zit hier vast.
for line in readfile:
    if search in line:
        print()
#ik close de file.
file1.close()
