#!/usr/bin/python3

#probeer te zoeken achter een string in dit geval invalid user

#ik zoek achter invalid user in mijn file (na veel verkeerd te hebben gezet en met veel opzoekwerk en veel proberen heb ik eindelijk alle invalid users er kunnen uithalen.
#what a relief (ik heb hier echt op liggen vloeken....)
with open("sshdlog", "r") as readfile:
    for line in readfile:
        line = line.strip()
        search= "Invalid user"
        if search in line:
            print(line)

#ik close de file.
readfile.close()
