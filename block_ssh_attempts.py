#!/usr/bin/python3

#probeer te zoeken achter een string in dit geval invalid user

#ik zoek achter invalid user in mijn file (na veel verkeerd te hebben gezet en met veel opzoekwerk en veel proberen heb ik eindelijk alle invalid users er kunnen uithalen.
#what a relief (ik heb hier echt op liggen vloeken....)
#ik heb een nieuwe lijn toegevoegd met split. hierin split ik elk woord en zie ik op welke plaats de ip adressen staan.
with open("sshdlog", "r") as readfile:
    for line in readfile:
        line = line.strip()
        search= "Invalid user"
        if search in line:
            #ik split de string in een lijst.
            line = line.split(" ")

            #ik draai de volgordevan de lijst om.
            line.reverse()
            #het IP Address staat altijd op de 3de plaats nu, dus deze selecteer ik.
            result = line[2]
            print(result)

        
