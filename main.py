#Russian and Korean alphabet trainer which mixes and matches latin alphabet to Korean and Russian alphabet to Korean.
#This trainer is for people who have already had a quick look at the letters before.

import datetime as dt
fortsette = True

print("Hei! i dette programmet kan du lære både en liten miks av Russisk alfabet og Koreans alfabet med mest fokus på")
print("det Koreanske alfabet. OBS! Du må kunne det Russiske alfabetet fra før av.")
vlstrt = input("Vil du starte? y/n ")

while fortsette:
    if vlstrt.lower() == "y":
        break
    print("La oss starte:")
    print("Det er 24 bokstaver i det Koreanske alfabetet.")
    elif vlstrt.lower() == "n":
    print("Greit. Start gjerne opp programmet igjen om du vil prøve.")
    else:
    print("Du tastet inn noe feil. Prøv igjen.")

