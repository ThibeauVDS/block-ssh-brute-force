#!/usr/bin/python3

#probeer te zoeken achter een string in dit geval invalid user

#ik zoek achter invalid user in mijn file (na veel verkeerd te hebben gezet en met veel opzoekwerk en veel proberen heb ik eindelijk alle invalid users er kunnen uithalen.
#what a relief (ik heb hier echt op liggen vloeken....)
#ik heb een nieuwe lijn toegevoegd met split. hierin split ik elk woord en zie ik op welke plaats de ip adressen staan.
import fwblock

invalid_ips = []

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
            invalid_ip = line[2]
            #print(invalid_ip)
            #de append zorgt ervoor dat de ipadressen in een lijst wordt toegevoegd.
            invalid_ips.append(invalid_ip)

for ip in set(invalid_ips):
    count = invalid_ips.count(ip)
    # als het 3 keer of meer voorkomt en het ip address steekt niet in de block (dit controleert hij dan) dan blokkeert hij het. 
    if count >= 3 and ip not in fwblock.blocked:
        fwblock.block_ip(ip)
        print(ip, "has been blocked!")


#print(fwblock.blocked) (controle middel)

   

